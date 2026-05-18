import torch
import requests
import hashlib
import json
from datetime import datetime, timedelta
from urllib.parse import urlparse
import re
import ssl
import socket

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

from database import SessionLocal, engine
from sqlalchemy import Column, String, Integer, DateTime, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Cache table
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
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# ========================
# TRUSTED DOMAINS
# ========================

TRUSTED_DOMAINS = [
    "google.com", "youtube.com", "github.com", "microsoft.com", 
    "amazon.com", "openai.com", "facebook.com", "instagram.com", 
    "wikipedia.org", "apple.com", "linkedin.com"
]

# ========================
# CACHE MANAGEMENT
# ========================

def get_cache(url):
    """Get cached prediction if exists and not expired (24 hours)."""
    db = SessionLocal()
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    
    cached = db.query(URLCache).filter(URLCache.url_hash == url_hash).first()
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

def cache_result(url, prediction, confidence, source):
    """Cache prediction result."""
    db = SessionLocal()
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    
    cached_entry = URLCache(
        url_hash=url_hash,
        url=url,
        prediction=prediction,
        confidence=confidence,
        source=source
    )
    db.add(cached_entry)
    db.commit()
    db.close()

# ========================
# URL FEATURE EXTRACTION
# ========================

def extract_url_features(url):
    """
    Extract features from URL for better classification.
    Returns feature score (0-1).
    """
    url_lower = url.lower()
    risk_score = 0.0
    
    parsed = urlparse(url)
    domain = parsed.netloc or url_lower
    
    # Suspicious domain patterns
    if len(domain) > 50:  # Unusually long domain
        risk_score += 0.1
    
    # Multiple subdomains (common in phishing)
    if domain.count('.') > 2:
        risk_score += 0.15
    
    # IP-based URLs (high risk)
    if re.match(r'.*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        risk_score += 0.3
    
    # Suspicious keywords in domain
    suspicious_keywords = ['bank', 'verify', 'confirm', 'login', 'secure', 'account', 'update', 'urgent']
    for keyword in suspicious_keywords:
        if keyword in url_lower and keyword not in TRUSTED_DOMAINS:
            risk_score += 0.05
    
    # URL shorteners (can hide malicious content)
    shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 'ow.ly']
    if any(shortener in url_lower for shortener in shorteners):
        risk_score += 0.2
    
    # Suspicious port
    if parsed.port and parsed.port not in [80, 443]:
        risk_score += 0.1
    
    # HTTPS check
    if not url.startswith('https://'):
        risk_score += 0.15
    
    return min(risk_score, 1.0)

def check_ssl_certificate(url):
    """Quick SSL certificate check (returns True if valid)."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=2) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return cert is not None
    except:
        return False

# ========================
# PHISHTANK CHECK
# ========================

def check_phishtank(url):
    """Check URL against PhishTank database with timeout."""
    try:
        response = requests.post(
            "https://checkurl.phishtank.com/checkurl/",
            data={"url": url, "format": "json"},
            timeout=3  # Reduced timeout for speed
        )
        
        result = response.json()
        return result.get("results", {}).get("in_database", False)
    except:
        return False

# ========================
# PREDICT URL
# ========================

def predict_url(url):
    """
    Predict if URL is phishing or safe using multi-stage detection.
    """
    url_lower = url.lower()
    
    # Check cache first
    cached = get_cache(url)
    if cached:
        return cached
    
    # Stage 1: Trusted domain check
    for domain in TRUSTED_DOMAINS:
        if domain in url_lower:
            result = {
                "prediction": "SAFE",
                "confidence": 0.99,
                "source": "trusted_domain"
            }
            cache_result(url, result["prediction"], result["confidence"], result["source"])
            return result
    
    # Stage 2: PhishTank check
    if check_phishtank(url):
        result = {
            "prediction": "PHISHING",
            "confidence": 0.999,
            "source": "phishtank"
        }
        cache_result(url, result["prediction"], result["confidence"], result["source"])
        return result
    
    # Stage 3: Feature-based detection
    feature_risk = extract_url_features(url)
    
    # Stage 4: Transformer AI
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
    probs = torch.softmax(logits, dim=1)
    
    prediction = torch.argmax(probs, dim=1).item()
    model_confidence = probs[0][prediction].item()
    
    # Combine model confidence with feature risk
    final_confidence = (model_confidence * 0.7) + (feature_risk * 0.3)
    
    result = {
        "prediction": "PHISHING" if prediction == 1 else "SAFE",
        "confidence": float(final_confidence),
        "source": "transformer_ai"
    }
    
    cache_result(url, result["prediction"], result["confidence"], result["source"])
    return result
