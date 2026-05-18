from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

import torch

# Load tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained(
    "atulak968/fraud-transformer"
)

# Load model
model = DistilBertForSequenceClassification.from_pretrained(
    ""atulak968/fraud-transformer""
)

# Prediction function
def predict_fraud(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        prediction = torch.argmax(
            outputs.logits,
            dim=1
        ).item()

        confidence = torch.softmax(
            outputs.logits,
            dim=1
        )[0][prediction].item()

    if prediction == 1:
        label = "SCAM"
    else:
        label = "SAFE"

    return {
        "prediction": label,
        "confidence": confidence
    }
