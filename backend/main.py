from database import engine
from database import SessionLocal

from models import Base
from models import Analysis

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile

from pydantic import BaseModel

import shutil

from image_detector import extract_text
from ensemble_inference import predict_fraud
from url_inference import predict_url

# ========================
# FASTAPI
# ========================

app = FastAPI()

# ========================
# CREATE DATABASE
# ========================

Base.metadata.create_all(bind=engine)

# ========================
# CORS
# ========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================
# REQUEST MODELS
# ========================

class Message(BaseModel):
    text: str

class URLRequest(BaseModel):
    url: str

# ========================
# CONFIDENCE THRESHOLDS
# ========================

CONFIDENCE_THRESHOLD = 0.65  # Below this = UNCERTAIN
HIGH_CONFIDENCE_THRESHOLD = 0.85

def get_alert_level(prediction, confidence):
    """Determine alert severity based on prediction and confidence."""
    if prediction == "SAFE":
        return "LOW"
    elif confidence >= HIGH_CONFIDENCE_THRESHOLD:
        return "HIGH"
    elif confidence >= CONFIDENCE_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"

def format_response(prediction, confidence, input_text, analysis_type):
    """Format response with confidence thresholds and metadata."""
    
    # Determine if prediction is reliable
    if confidence < CONFIDENCE_THRESHOLD:
        status = "UNCERTAIN"
        alert_level = "LOW"
    else:
        status = "RELIABLE"
        alert_level = get_alert_level(prediction, confidence)
    
    return {
        "prediction": prediction,
        "confidence": round(confidence, 4),
        "status": status,
        "alert_level": alert_level,
        "recommendation": "REVIEW_MANUALLY" if status == "UNCERTAIN" else "PROCEED_WITH_CAUTION" if alert_level == "HIGH" else "SAFE"
    }

# ========================
# HOME ROUTE
# ========================

@app.get("/")
def home():
    return {
        "message": "AI Cyber Forensics API Running",
        "version": "2.0",
        "features": ["text_detection", "image_ocr", "url_analysis", "caching"]
    }

# ========================
# TEXT FRAUD DETECTION
# ========================

@app.post("/detect")
def detect(message: Message):
    
    result = predict_fraud(message.text)
    prediction = result["prediction"]
    confidence = result["confidence"]
    
    # Format with thresholds
    response = format_response(prediction, confidence, message.text, "TEXT")
    
    # Save to database
    db = SessionLocal()
    analysis = Analysis(
        input_text=message.text,
        prediction=prediction,
        confidence=confidence,
        analysis_type="TEXT"
    )
    db.add(analysis)
    db.commit()
    db.close()
    
    return response

# ========================
# OCR IMAGE ANALYSIS
# ========================

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    
    # Save image
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # OCR extraction with cleaning
    extracted_text = extract_text(file_path)
    
    # Fraud prediction
    result = predict_fraud(extracted_text)
    prediction = result["prediction"]
    confidence = result["confidence"]
    
    # Format with thresholds
    response = format_response(prediction, confidence, extracted_text, "OCR")
    response["extracted_text"] = extracted_text
    response["filename"] = file.filename
    
    # Save to database
    db = SessionLocal()
    analysis = Analysis(
        input_text=extracted_text,
        prediction=prediction,
        confidence=confidence,
        analysis_type="OCR"
    )
    db.add(analysis)
    db.commit()
    db.close()
    
    # Cleanup temp file
    import os
    try:
        os.remove(file_path)
    except:
        pass
    
    return response

# ========================
# URL ANALYSIS
# ========================

@app.post("/analyze-url")
def analyze_url(request: URLRequest):
    
    result = predict_url(request.url)
    prediction = result["prediction"]
    confidence = result["confidence"]
    source = result.get("source", "unknown")
    
    # Format with thresholds
    response = format_response(prediction, confidence, request.url, "URL")
    response["url"] = request.url
    response["source"] = source
    
    # Save to database
    db = SessionLocal()
    analysis = Analysis(
        input_text=request.url,
        prediction=prediction,
        confidence=confidence,
        analysis_type="URL"
    )
    db.add(analysis)
    db.commit()
    db.close()
    
    return response

# ========================
# HISTORY API
# ========================

@app.get("/history")
def history():
    
    db = SessionLocal()
    
    results = db.query(Analysis)\
        .order_by(Analysis.id.desc())\
        .limit(10)\
        .all()
    
    history_data = []
    
    for item in results:
        history_data.append({
            "id": item.id,
            "input_text": item.input_text[:100],  # Truncate for privacy
            "prediction": item.prediction,
            "confidence": round(item.confidence, 4),
            "analysis_type": item.analysis_type,
            "timestamp": item.created_at.isoformat() if hasattr(item, 'created_at') else None
        })
    
    db.close()
    
    return {"history": history_data}

# ========================
# HEALTH CHECK
# ========================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "cache_enabled": True,
        "url_features_enabled": True,
        "ocr_cleaning_enabled": True
    }
