from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .database import (
    save_user, save_plan, get_user, get_original_plan,
    update_plan, get_all_users, delete_user
)
from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    username: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: str = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    plan = generate_workout_gemini(username, age, weight, goal, intensity)
    tip = generate_nutrition_tip_with_flash(goal)

    save_user(user_id, username, age, weight, goal, intensity)
    save_plan(user_id, plan, tip)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "user": get_user(user_id),
            "workout_plan": plan,
            "nutrition_tip": tip,
            "message": None,
        },
    )


@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):
    user = get_user(user_id)
    if not user:
        return templates.TemplateResponse(
            request=request,
            name="feedback.html",
            context={"request": request, "error": "User ID not found. Please generate a plan first."},
            status_code=404,
        )

    updated = update_workout_plan(user.original_plan, feedback)
    update_plan(user_id, updated, feedback)
    refreshed = get_user(user_id)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "user": refreshed,
            "workout_plan": updated,
            "nutrition_tip": refreshed.nutrition_tip,
            "message": "Your workout plan was updated using your feedback.",
        },
    )


@router.get("/feedback", response_class=HTMLResponse)
def feedback_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="feedback.html",
        context={"request": request},
    )


@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={"request": request, "users": get_all_users()},
    )


@router.post("/delete-user/{user_id}")
def remove_user(user_id: str):
    delete_user(user_id)
    return RedirectResponse(url="/view-all-users", status_code=303)
