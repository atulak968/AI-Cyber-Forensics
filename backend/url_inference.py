import torch
import requests
import hashlib
import re
import ssl
import socket

from datetime import datetime, timedelta
from urllib.parse import urlparse

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

from database import SessionLocal, engine
from sqlalchemy import Column, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ========================
# CACHE TABLE
# ========================

class URLCache(Base):

    __tablename__ = "url_cache"

    url_hash = Column(String, primary_key=True)
    url = Column(String)
    prediction = Column(String)
    confidence = Column(Float)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# ========================
# LOAD MODEL
# ========================

MODEL_PATH = "atulak968/url-transformer"

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()

# ========================
# TRUSTED DOMAINS
# ========================

TRUSTED_DOMAINS = [

    "google.com",
    "youtube.com",
    "github.com",
    "microsoft.com",
    "amazon.com",
    "openai.com",
    "chatgpt.com",
    "railway.app",
    "vercel.app",
    "facebook.com",
    "instagram.com",
    "wikipedia.org",
    "apple.com",
    "linkedin.com",

]

# ========================
# CACHE
# ========================

def get_cache(url):

    db = SessionLocal()

    url_hash = hashlib.sha256(
        url.encode()
    ).hexdigest()

    cached = db.query(URLCache).filter(
        URLCache.url_hash == url_hash
    ).first()

    db.close()

    if cached:

        age = datetime.utcnow() - cached.created_at

        if age < timedelta(hours=24):

            return {
                "prediction": cached.prediction,
                "confidence": cached.confidence,
                "source": cached.source + "_cached"
            }

    return None


def cache_result(
    url,
    prediction,
    confidence,
    source
):

    db = SessionLocal()

    url_hash = hashlib.sha256(
        url.encode()
    ).hexdigest()

    entry = URLCache(
        url_hash=url_hash,
        url=url,
        prediction=prediction,
        confidence=confidence,
        source=source
    )

    db.add(entry)

    db.commit()

    db.close()

# ========================
# URL FEATURES
# ========================

def extract_url_features(url):

    url_lower = url.lower()

    parsed = urlparse(url)

    domain = parsed.netloc

    risk_score = 0.0

    # Long domain

    if len(domain) > 50:
        risk_score += 0.1

    # Too many subdomains

    if domain.count(".") > 3:
        risk_score += 0.15

    # IP address URL

    if re.match(
        r".*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
        url
    ):
        risk_score += 0.3

    # Suspicious keywords

    suspicious_keywords = [

        "verify",
        "bank",
        "secure",
        "account",
        "update",
        "login",
        "urgent",
        "confirm",
        "gift",
        "free",
        "bonus",

    ]

    for keyword in suspicious_keywords:

        if keyword in url_lower:
            risk_score += 0.05

    # URL shorteners

    shorteners = [

        "bit.ly",
        "tinyurl",
        "goo.gl",
        "ow.ly",

    ]

    if any(
        short in url_lower
        for short in shorteners
    ):
        risk_score += 0.2

    # No HTTPS

    if not url.startswith("https://"):
        risk_score += 0.15

    return min(risk_score, 1.0)

# ========================
# SSL CHECK
# ========================

def check_ssl_certificate(url):

    try:

        parsed = urlparse(url)

        domain = parsed.netloc

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain, 443),
            timeout=2
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

                return cert is not None

    except:
        return False

# ========================
# PHISHTANK
# ========================

def check_phishtank(url):

    try:

        response = requests.post(

            "https://checkurl.phishtank.com/checkurl/",

            data={
                "url": url,
                "format": "json"
            },

            timeout=3
        )

        result = response.json()

        return result.get(
            "results",
            {}
        ).get(
            "in_database",
            False
        )

    except:
        return False

# ========================
# MAIN PREDICTION
# ========================

def predict_url(url):

    url_lower = url.lower()

    parsed = urlparse(url)

    hostname = parsed.netloc.lower()

    # ------------------------
    # CACHE
    # ------------------------

    cached = get_cache(url)

    if cached:
        return cached

    # ------------------------
    # TRUSTED DOMAIN CHECK
    # ------------------------

    for domain in TRUSTED_DOMAINS:

        if (
            hostname == domain
            or hostname.endswith("." + domain)
        ):

            result = {
                "prediction": "SAFE",
                "confidence": 0.99,
                "source": "trusted_domain"
            }

            cache_result(
                url,
                result["prediction"],
                result["confidence"],
                result["source"]
            )

            return result

    # ------------------------
    # PHISHTANK
    # ------------------------

    if check_phishtank(url):

        result = {
            "prediction": "PHISHING",
            "confidence": 0.999,
            "source": "phishtank"
        }

        cache_result(
            url,
            result["prediction"],
            result["confidence"],
            result["source"]
        )

        return result

    # ------------------------
    # FEATURE ENGINE
    # ------------------------

    feature_risk = extract_url_features(url)

    # ------------------------
    # TRANSFORMER MODEL
    # ------------------------

    inputs = tokenizer(

        url,

        return_tensors="pt",

        truncation=True,

        padding=True,

        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

    logits = outputs.logits

    probs = torch.softmax(
        logits,
        dim=1
    )

    prediction = torch.argmax(
        probs,
        dim=1
    ).item()

    model_confidence = probs[
        0
    ][prediction].item()

    print("RAW PREDICTION:", prediction)

    print("MODEL CONFIDENCE:", model_confidence)

    # ========================
    # LABEL FIX
    # ========================

    # IMPORTANT:
    # Your model labels appear reversed

    final_prediction = (
        "SAFE"
        if prediction == 1
        else "PHISHING"
    )

    # ------------------------
    # FINAL CONFIDENCE
    # ------------------------

    final_confidence = (
        model_confidence * 0.7
        + feature_risk * 0.3
    )

    # ------------------------
    # FINAL RESULT
    # ------------------------

    result = {

        "prediction": final_prediction,

        "confidence": float(
            final_confidence
        ),

        "source": "transformer_ai"
    }

    cache_result(

        url,

        result["prediction"],

        result["confidence"],

        result["source"]
    )

    return result