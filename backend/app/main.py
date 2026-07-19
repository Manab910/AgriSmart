from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.predict import router as predict_router

app = FastAPI(
    title="AgriSmart AI",
    version="1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://agri-smart-ai-pg35.vercel.app",
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(predict_router)

# Home Route
@app.get("/")
def home():
    return {
        "message": "AgriSmart AI API Running"
    }
