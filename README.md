# FitBuddy – AI Fitness Plan Generator using Gemini Models

A FastAPI + Jinja2 + SQLite + SQLAlchemy web application inspired by the SmartBridge FitBuddy project document.

## Features
- User input: name, user ID, age, weight, fitness goal and workout intensity
- AI-generated 7-day workout plan
- AI nutrition/recovery tip
- Feedback-based workout plan update
- SQLite persistence
- Admin view of users and original/updated plans
- FastAPI interactive API docs
- Responsive HTML/CSS interface

## Project structure
- `app/main.py` – FastAPI application and routes
- `app/database.py` – SQLAlchemy/SQLite persistence
- `app/gemini_generator.py` – workout generation
- `app/gemini_flash_generator.py` – nutrition/recovery tip
- `app/updated_plan.py` – feedback-based plan update
- `templates/` – Jinja2 pages
- `static/` – CSS/JS assets

## Run locally (Windows)
1. Install Python 3.10+.
2. Open terminal in this folder.
3. Create a virtual environment:
   `python -m venv venv`
4. Activate:
   `venv\Scripts\activate`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Copy `.env.example` to `.env`.
7. Put your Gemini API key in `.env`:
   `GOOGLE_API_KEY=your_key`
8. Start:
   `uvicorn app.main:app --reload`
9. Open:
   `http://127.0.0.1:8000`
10. API docs:
   `http://127.0.0.1:8000/docs`

## Linux/macOS
Activate with:
`source venv/bin/activate`

## Demo without an API key
The application includes a clearly labeled demo/fallback mode. If `GOOGLE_API_KEY` is missing or an AI request fails, it returns a sample generated plan so the UI can still be demonstrated locally.

## Important
This is an educational fitness-planning project. AI output is not medical advice. Users should consult a qualified healthcare/fitness professional for medical conditions, injuries, or individualized clinical guidance.
