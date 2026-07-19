import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

print("=" * 60)
print("BASE_DIR:", BASE_DIR)

MODELS_DIR = os.path.join(BASE_DIR, "models")

print("MODELS_DIR:", MODELS_DIR)
print("Models folder exists:", os.path.exists(MODELS_DIR))

if os.path.exists(MODELS_DIR):
    print("Files:", os.listdir(MODELS_DIR))

MODEL_PATH = os.path.join(MODELS_DIR, "best_model.pkl")
ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")

print("MODEL_PATH:", MODEL_PATH)
print("MODEL EXISTS:", os.path.exists(MODEL_PATH))

print("ENCODER EXISTS:", os.path.exists(ENCODER_PATH))

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)