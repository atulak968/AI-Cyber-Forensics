"""
Ensemble model for fraud detection combining DistilBERT with feature-based rules.
"""
import torch
import numpy as np
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

# ========================
# LOAD MODELS
# ========================

# Model 1: DistilBERT (main model)
distilbert_tokenizer = DistilBertTokenizerFast.from_pretrained(
    "../models/fraud_transformer"
)
distilbert_model = DistilBertForSequenceClassification.from_pretrained(
    "../models/fraud_transformer"
)
distilbert_model.eval()

# ========================
# ENSEMBLE PREDICTION
# ========================

def predict_fraud_ensemble(text):
    """
    Ensemble prediction combining DistilBERT with rule-based features.
    Returns weighted average confidence.
    """
    predictions = []
    confidences = []
    
    # Model 1: DistilBERT
    distilbert_pred, distilbert_conf = predict_with_distilbert(text)
    predictions.append(distilbert_pred)
    confidences.append(distilbert_conf * 0.70)  # 70% weight
    
    # Model 2: Feature-based rules (heuristics)
    rule_pred, rule_conf = predict_with_features(text)
    predictions.append(rule_pred)
    confidences.append(rule_conf * 0.30)  # 30% weight
    
    # Aggregate predictions
    avg_confidence = sum(confidences)
    
    # Majority voting for prediction
    scam_votes = sum(1 for p in predictions if p == "SCAM")
    final_prediction = "SCAM" if scam_votes >= 2 else "SAFE"
    
    return {
        "prediction": final_prediction,
        "confidence": min(avg_confidence, 0.99),  # Cap at 0.99
        "ensemble_votes": {"SCAM": scam_votes, "SAFE": len(predictions) - scam_votes}
    }

def predict_with_distilbert(text):
    """DistilBERT prediction."""
    inputs = distilbert_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )
    
    with torch.no_grad():
        outputs = distilbert_model(**inputs)
        logits = outputs.logits
        confidence = torch.softmax(logits, dim=1)[0]
        prediction_id = torch.argmax(confidence).item()
        confidence_score = confidence[prediction_id].item()
    
    prediction = "SCAM" if prediction_id == 1 else "SAFE"
    return prediction, confidence_score

def predict_with_features(text):
    """
    Rule-based prediction using fraud indicators.
    """
    text_lower = text.lower()
    risk_score = 0.0
    
    # Urgency indicators
    urgency_words = ["urgent", "immediately", "now", "asap", "hurry", "limited time", "act now"]
    for word in urgency_words:
        if word in text_lower:
            risk_score += 0.1
    
    # Money-related suspicious phrases
    money_phrases = ["click here", "win", "congratulations", "claim", "free money", "guarantee"]
    for phrase in money_phrases:
        if phrase in text_lower:
            risk_score += 0.1
    
    # Request for personal info
    info_requests = ["password", "credit card", "social security", "bank account", "verify identity"]
    for info in info_requests:
        if info in text_lower:
            risk_score += 0.15
    
    # Suspicious grammar/spelling markers
    suspicious_markers = ["re-activate", "confirm ur", "click belo", "verifiy", "update ur account"]
    for marker in suspicious_markers:
        if marker in text_lower:
            risk_score += 0.1
    
    # Text length analysis
    if len(text) < 20 or len(text) > 5000:
        risk_score += 0.05
    
    # Cap risk score
    risk_score = min(risk_score, 0.99)
    
    prediction = "SCAM" if risk_score > 0.5 else "SAFE"
    return prediction, risk_score

# ========================
# MAIN PREDICTION FUNCTION
# ========================

def predict_fraud(text):
    """
    Main prediction function using ensemble approach.
    """
    try:
        result = predict_fraud_ensemble(text)
        return {
            "prediction": result["prediction"],
            "confidence": result["confidence"]
        }
    except Exception as e:
        print(f"Ensemble error: {e}, falling back to DistilBERT")
        pred, conf = predict_with_distilbert(text)
        return {
            "prediction": pred,
            "confidence": conf
        }
