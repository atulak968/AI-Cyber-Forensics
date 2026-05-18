# AI Cyber Forensics Platform 🚀

Advanced Multi-Modal AI Cybersecurity Intelligence System

---

# Overview

AI Cyber Forensics Platform is a full-stack AI-powered cybersecurity system designed to detect:

- Scam messages
- Phishing URLs
- Fraud screenshots
- OCR-based scams
- Social engineering attacks

The platform combines:

- Artificial Intelligence
- Transformer Models
- OCR
- Threat Intelligence
- FastAPI Backend
- Next.js Frontend

---

# Features 🔥

## AI Scam Text Detection

Analyze suspicious:

- emails
- SMS
- chats
- phishing messages

using transformer-based AI.

---

## OCR Fraud Detection

Upload screenshots for:

- fake payment detection
- scam chats
- phishing screenshots
- fraud banking screenshots

The system extracts text using OCR and analyzes fraud patterns.

---

## URL Phishing Detection

Detect malicious URLs using:

- Transformer AI
- Threat Intelligence
- Trusted Domain Verification
- PhishTank Integration

Example:

```text
http://secure-paytm-login-freegift.xyz
```

---

## Threat Intelligence Engine

Integrated with:

- PhishTank

Supports:

- phishing detection
- threat reputation
- cyber intelligence workflows

---

## Real-Time Dashboard

Cybersecurity dashboard includes:

- Threat statistics
- URL analysis
- OCR analysis
- Threat activity history
- Fraud confidence scores

---

# Tech Stack 🚀

## Frontend

- Next.js 16
- React 19
- Tailwind CSS
- TypeScript

---

## Backend

- FastAPI
- Python
- SQLAlchemy
- SQLite
- Uvicorn

---

## AI / ML

- DistilBERT
- HuggingFace Transformers
- OCR Engine
- Transformer URL Detection
- Threat Intelligence APIs

---

# Project Structure

```text
AI-Cyber-Forensics/
│
├── backend/
│   ├── main.py
│   ├── transformer_inference.py
│   ├── url_inference.py
│   ├── image_detector.py
│   ├── database.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── public/
│
├── models/
├── datasets/
└── README.md
```

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/atulak968/AI-Cyber-Forensics.git
```

```bash
cd AI-Cyber-Forensics
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
cd backend
```

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

Open new terminal.

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# AI Models Used

## Scam Detection Model

Transformer:

```text
DistilBERT
```

Datasets:

- Enron
- CEAS
- SpamAssassin
- Nigerian Fraud
- Phishing Email Datasets

---

## URL Detection Model

Transformer-based phishing URL classifier trained on large phishing datasets.

---

# API Endpoints

## Text Analysis

```http
POST /detect
```

---

## OCR Analysis

```http
POST /analyze-image
```

---

## URL Analysis

```http
POST /analyze-url
```

---

## Threat History

```http
GET /history
```

---

# Deployment 🚀

## Frontend

Recommended:

- Vercel

---

## Backend

Recommended:

- Railway
- Render

---

# Future Improvements

- QR Code Fraud Detection
- VirusTotal Integration
- AbuseIPDB Integration
- PDF Forensic Reports
- Real-Time Alerts
- Vision Transformer Models
- Investigator Case Management
- Multi-language Scam Detection

---

# Screenshots

## Dashboard

(Add screenshots here)

---

# Learning Outcomes

This project demonstrates:

- AI model training
- Transformer fine-tuning
- OCR pipelines
- Cybersecurity workflows
- Threat intelligence systems
- Full-stack engineering
- REST API development
- Database integration

---

# Author

Atul Kumar

AI + Cybersecurity Engineering Project 🚀
