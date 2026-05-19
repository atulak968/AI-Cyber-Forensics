import pytesseract
import cv2
import numpy as np

from PIL import Image
from io import BytesIO

# =========================
# OCR + SCAM DETECTION
# =========================

SCAM_KEYWORDS = [

    "otp",
    "bank",
    "verify",
    "urgent",
    "gift",
    "free",
    "winner",
    "lottery",
    "account blocked",
    "click link",
    "password",
    "claim now",
]

# =========================
# MAIN ANALYZER
# =========================

def analyze_image_contents(image_bytes):

    try:

        # =========================
        # LOAD IMAGE
        # =========================

        image = Image.open(
            BytesIO(image_bytes)
        ).convert("RGB")

        # =========================
        # CONVERT TO OPENCV
        # =========================

        image_np = np.array(image)

        gray = cv2.cvtColor(
            image_np,
            cv2.COLOR_RGB2GRAY
        )

        # =========================
        # OCR
        # =========================

        extracted_text = pytesseract.image_to_string(
            gray
        )

        extracted_text_lower = (
            extracted_text.lower()
        )

        # =========================
        # SCAM SCORE
        # =========================

        score = 0

        found_keywords = []

        for keyword in SCAM_KEYWORDS:

            if keyword in extracted_text_lower:

                score += 1

                found_keywords.append(keyword)

        # =========================
        # CONFIDENCE
        # =========================

        confidence = min(
            0.5 + (score * 0.1),
            0.99
        )

        # =========================
        # PREDICTION
        # =========================

        prediction = (
            "SCAM IMAGE"
            if score >= 2
            else "SAFE IMAGE"
        )

        return {

            "prediction": prediction,

            "confidence": confidence,

            "keywords_detected": found_keywords,

            "extracted_text": extracted_text
        }

    except Exception as e:

        print("OCR ERROR:", str(e))

        return {

            "prediction": "ERROR",

            "confidence": 0.0,

            "keywords_detected": [],

            "extracted_text": "",

            "error": str(e)
        }