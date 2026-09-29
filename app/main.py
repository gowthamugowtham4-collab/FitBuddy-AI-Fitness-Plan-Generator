from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import router

app = FastAPI(
    title="FitBuddy – AI Fitness Plan Generator",
    description="AI-powered personalized fitness planning using Gemini models.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
