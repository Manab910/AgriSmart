from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URI, DATABASE_NAME

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]

predictions_collection = db["predictions"]
weather_collection = db["weather"]
model_results_collection = db["model_results"]