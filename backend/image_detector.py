import pytesseract
from PIL import Image
from textblob import TextBlob
import re

def extract_text(image_path):
    """
    Extract text from image using OCR and apply cleaning.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    
    # Clean extracted text
    cleaned_text = clean_ocr_text(text)
    return cleaned_text

def clean_ocr_text(text):
    """
    Clean OCR output: remove artifacts, fix spelling, normalize formatting.
    """
    if not text:
        return text
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove common OCR artifacts (|, ~, etc.)
    text = re.sub(r'[|~`^]', '', text)
    
    # Fix broken lines
    text = re.sub(r'([a-z])-\s+([a-z])', r'\1\2', text)
    
    # Correct spelling (lightweight - for fraud indicators)
    blob = TextBlob(text)
    text = str(blob.correct())
    
    # Remove excessive punctuation
    text = re.sub(r'([!?.]){2,}', r'\1', text)
    
    return text
