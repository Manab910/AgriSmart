from fastapi import APIRouter
import pandas as pd
import numpy as np

from app.schemas import CropInput
from app.model_loader import model, label_encoder

router = APIRouter()

@router.post("/predict-crop")
def predict_crop(data: CropInput):

    input_data = pd.DataFrame([{
        "N": data.N,
        "P": data.P,
        "K": data.K,
        "temperature": data.temperature,
        "humidity": data.humidity,
        "ph": data.ph,
        "rainfall": data.rainfall
    }])

    prediction = model.predict(input_data)
    crop = label_encoder.inverse_transform(prediction)[0]

    confidence = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)
        confidence = round(float(np.max(probabilities)) * 100, 2)

    return {
        "recommended_crop": crop,
        "confidence": confidence,
        "temperature": data.temperature,
        "humidity": data.humidity,
        "rainfall": data.rainfall,
        "message": f"{crop} is the most suitable crop for the given soil and weather conditions."
    }