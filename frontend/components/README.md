# AI Cyber Forensics Platform 🚀

## Project Overview

AI Cyber Forensics Platform is a multi-modal cybersecurity intelligence system designed to detect:

* Scam messages
* Phishing URLs
* Fraud screenshots
* OCR-based scam content
* Social engineering attacks

The project combines:

* Artificial Intelligence
* Transformer Models
* OCR (Optical Character Recognition)
* Threat Intelligence
* FastAPI Backend
* Next.js Frontend
* SQLite Database

The goal of this project is to simulate a real-world cyber defense platform similar to enterprise SOC (Security Operations Center) systems.

---

# Technologies Used

## Frontend

| Technology   | Purpose               |
| ------------ | --------------------- |
| Next.js 16   | Frontend framework    |
| React 19     | UI library            |
| Tailwind CSS | Styling               |
| TypeScript   | Component development |

---

## Backend

| Technology | Purpose                     |
| ---------- | --------------------------- |
| FastAPI    | High-performance API server |
| Python     | Backend programming         |
| Uvicorn    | ASGI server                 |
| SQLAlchemy | Database ORM                |
| SQLite     | Local database              |

---

## AI / Machine Learning

| Technology               | Purpose                |
| ------------------------ | ---------------------- |
| DistilBERT               | Scam text detection    |
| HuggingFace Transformers | Transformer framework  |
| OCR Engine               | Image text extraction  |
| Transformer URL Model    | Phishing URL detection |
| Threat Intelligence      | PhishTank integration  |

---

# Features Implemented

## 1. Text Scam Detection

Users can paste suspicious messages.

The AI model analyzes:

* Scam language
* Social engineering patterns
* Fraud indicators

Example:

```text
URGENT: verify your banking account immediately
```

Output:

```text
SCAM
Confidence: 99%
```

---

## 2. OCR Screenshot Fraud Detection

Users upload screenshots.

The system:

1. Extracts text using OCR
2. Sends extracted text to transformer model
3. Detects fraud patterns

Supports:

* Fake payment screenshots
* Scam chats
* Fraud banking screenshots

---

## 3. URL Phishing Detection

The system analyzes URLs using:

* Transformer-based AI
* Trusted domain verification
* Threat intelligence
* PhishTank integration

Example:

```text
http://secure-paytm-login-freegift.xyz
```

Output:

```text
PHISHING
Confidence: 99%
```

---

## 4. Threat Intelligence Engine

Integrated with:

* PhishTank

This allows detection of:

* Known phishing websites
* Threat reputation
* Real-world cyber intelligence

---

## 5. Dashboard Interface

Modern cybersecurity dashboard including:

* Live statistics
* Threat activity
* URL analyzer
* OCR analyzer
* Scam detection panel

---

## 6. Database Logging

All analyses are stored in SQLite database.

Stored information:

* Input data
* Prediction
* Confidence score
* Analysis type

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
│   ├── cyber_forensics.db
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── tailwind.config.js
│
├── datasets/
│   ├── phishing_email.csv
│   ├── phishing.csv
│   ├── new_data_urls.csv
│   └── vision_fraud_dataset/
│
├── models/
│   ├── fraud_transformer/
│   └── url_transformer/
│
└── README.md
```

---

# Why This Project Was Built

This project was built to:

* Learn AI security engineering
* Explore phishing detection systems
* Build real-world cybersecurity AI workflows
* Practice transformer model training
* Create a professional portfolio project
* Simulate enterprise SOC platforms

---

# AI Models Used

## Scam Text Detection

Model:

```text
DistilBERT
```

Dataset Sources:

* Enron
* CEAS
* Nigerian Fraud
* SpamAssassin
* Phishing email datasets

---

## URL Detection Model

Transformer trained on:

```text
new_data_urls.csv
```

Capabilities:

* Detect phishing domains
* Detect suspicious URL structures
* Detect scam patterns

---

# How To Run The Project Locally

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO
cd AI-Cyber-Forensics
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

## 4. Run Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## 5. Run Frontend

Open new terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

# How To Upload To GitHub

## Step 1 — Initialize Git

Inside project root:

```bash
git init
```

---

## Step 2 — Create .gitignore

Create file:

```text
.gitignore
```

Add:

```gitignore
.venv
node_modules
.next
__pycache__
*.db
```

---

## Step 3 — Add Files# AI Cyber Forensics Platform 🚀

## Project Overview

AI Cyber Forensics Platform is a multi-modal cybersecurity intelligence system designed to detect:

* Scam messages
* Phishing URLs
* Fraud screenshots
* OCR-based scam content
* Social engineering attacks

The project combines:

* Artificial Intelligence
* Transformer Models
* OCR (Optical Character Recognition)
* Threat Intelligence
* FastAPI Backend
* Next.js Frontend
* SQLite Database

The goal of this project is to simulate a real-world cyber defense platform similar to enterprise SOC (Security Operations Center) systems.

---

# Technologies Used

## Frontend

| Technology   | Purpose               |
| ------------ | --------------------- |
| Next.js 16   | Frontend framework    |
| React 19     | UI library            |
| Tailwind CSS | Styling               |
| TypeScript   | Component development |

---

## Backend

| Technology | Purpose                     |
| ---------- | --------------------------- |
| FastAPI    | High-performance API server |
| Python     | Backend programming         |
| Uvicorn    | ASGI server                 |
| SQLAlchemy | Database ORM                |
| SQLite     | Local database              |

---

## AI / Machine Learning

| Technology               | Purpose                |
| ------------------------ | ---------------------- |
| DistilBERT               | Scam text detection    |
| HuggingFace Transformers | Transformer framework  |
| OCR Engine               | Image text extraction  |
| Transformer URL Model    | Phishing URL detection |
| Threat Intelligence      | PhishTank integration  |

---

# Features Implemented

## 1. Text Scam Detection

Users can paste suspicious messages.

The AI model analyzes:

* Scam language
* Social engineering patterns
* Fraud indicators

Example:

```text
URGENT: verify your banking account immediately
```

Output:

```text
SCAM
Confidence: 99%
```

---

## 2. OCR Screenshot Fraud Detection

Users upload screenshots.

The system:

1. Extracts text using OCR
2. Sends extracted text to transformer model
3. Detects fraud patterns

Supports:

* Fake payment screenshots
* Scam chats
* Fraud banking screenshots

---

## 3. URL Phishing Detection

The system analyzes URLs using:

* Transformer-based AI
* Trusted domain verification
* Threat intelligence
* PhishTank integration

Example:

```text
http://secure-paytm-login-freegift.xyz
```

Output:

```text
PHISHING
Confidence: 99%
```

---

## 4. Threat Intelligence Engine

Integrated with:

* PhishTank

This allows detection of:

* Known phishing websites
* Threat reputation
* Real-world cyber intelligence

---

## 5. Dashboard Interface

Modern cybersecurity dashboard including:

* Live statistics
* Threat activity
* URL analyzer
* OCR analyzer
* Scam detection panel

---

## 6. Database Logging

All analyses are stored in SQLite database.

Stored information:

* Input data
* Prediction
* Confidence score
* Analysis type

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
│   ├── cyber_forensics.db
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── tailwind.config.js
│
├── datasets/
│   ├── phishing_email.csv
│   ├── phishing.csv
│   ├── new_data_urls.csv
│   └── vision_fraud_dataset/
│
├── models/
│   ├── fraud_transformer/
│   └── url_transformer/
│
└── README.md
```

---

# Why This Project Was Built

This project was built to:

* Learn AI security engineering
* Explore phishing detection systems
* Build real-world cybersecurity AI workflows
* Practice transformer model training
* Create a professional portfolio project
* Simulate enterprise SOC platforms

---

# AI Models Used

## Scam Text Detection

Model:

```text
DistilBERT
```

Dataset Sources:

* Enron
* CEAS
* Nigerian Fraud
* SpamAssassin
* Phishing email datasets

---

## URL Detection Model

Transformer trained on:

```text
new_data_urls.csv
```

Capabilities:

* Detect phishing domains
* Detect suspicious URL structures
* Detect scam patterns

---

# How To Run The Project Locally

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO
cd AI-Cyber-Forensics
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

## 4. Run Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## 5. Run Frontend

Open new terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

# How To Upload To GitHub

## Step 1 — Initialize Git

Inside project root:

```bash
git init
```

---

## Step 2 — Create .gitignore

Create file:

```text
.gitignore
```

Add:

```gitignore
.venv
node_modules
.next
__pycache__
*.db
```

---

## Step 3 — Add Files

```bash
git add .
```

---

## Step 4 — Commit

```bash
git commit -m "Initial commit"
```

---

## Step 5 — Create GitHub Repository

Go to:

[https://github.com](https://github.com)

Create new repository.

Example:

```text
AI-Cyber-Forensics
```

---

## Step 6 — Connect Repository

```bash
git branch -M main
```

```bash
git remote add origin YOUR_REPOSITORY_URL
```

Example:

```bash
git remote add origin https://github.com/username/AI-Cyber-Forensics.git
```

---

## Step 7 — Push To GitHub

```bash
git push -u origin main
```

---

# Deployment Guide

## Frontend Deployment

Recommended:

* Vercel

Why:

* Best for Next.js
* Easy GitHub integration
* Free hosting

Deployment Steps:

1. Login to Vercel
2. Import GitHub repository
3. Select frontend folder
4. Deploy

---

## Backend Deployment

Recommended:

* Railway
* Render

Backend Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# Future Improvements

## Planned Features

* QR code fraud detection
* VirusTotal integration
* AbuseIPDB integration
* Investigator case management
* PDF forensic reports
* Real-time alerts
* Vision transformer fraud detection
* Indic language scam detection

---

# Learning Outcomes

This project demonstrates:

* AI model training
* Transformer fine-tuning
* OCR pipelines
* Threat intelligence systems
* Cybersecurity workflows
* Full-stack development
* Database integration
* REST API development
* Production-style architecture

---

# Final Result

This project evolved into a:

# Multi-Modal AI Cybersecurity Intelligence Platform

Combining:

* Artificial Intelligence
* Cybersecurity
* Threat Intelligence
* OCR Analysis
* Transformer Models
* Full-Stack Engineering

🚀


```bash
git add .
```

---

## Step 4 — Commit

```bash
git commit -m "Initial commit"
```

---

## Step 5 — Create GitHub Repository

Go to:

[https://github.com](https://github.com)

Create new repository.

Example:

```text
AI-Cyber-Forensics
```

---

## Step 6 — Connect Repository

```bash
git branch -M main
```

```bash
git remote add origin YOUR_REPOSITORY_URL
```

Example:

```bash
git remote add origin https://github.com/username/AI-Cyber-Forensics.git
```

---

## Step 7 — Push To GitHub

```bash
git push -u origin main
```

---

# Deployment Guide

## Frontend Deployment

Recommended:

* Vercel

Why:

* Best for Next.js
* Easy GitHub integration
* Free hosting

Deployment Steps:

1. Login to Vercel
2. Import GitHub repository
3. Select frontend folder
4. Deploy

---

## Backend Deployment

Recommended:

* Railway
* Render

Backend Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# Future Improvements

## Planned Features

* QR code fraud detection
* VirusTotal integration
* AbuseIPDB integration
* Investigator case management
* PDF forensic reports
* Real-time alerts
* Vision transformer fraud detection
* Indic language scam detection

---

# Learning Outcomes

This project demonstrates:

* AI model training
* Transformer fine-tuning
* OCR pipelines
* Threat intelligence systems
* Cybersecurity workflows
* Full-stack development
* Database integration
* REST API development
* Production-style architecture

---

# Final Result

This project evolved into a:

# Multi-Modal AI Cybersecurity Intelligence Platform

Combining:

* Artificial Intelligence
* Cybersecurity
* Threat Intelligence
* OCR Analysis
* Transformer Models
* Full-Stack Engineering

🚀
