import os
import google.generativeai as genai

def update_workout_plan(original_plan, feedback):
    fallback = original_plan + f"\n\nFEEDBACK UPDATE\nUser feedback: {feedback}\n\nPlease apply the requested changes gradually and safely."
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return fallback

    try:
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-1.5-pro")
        model = genai.GenerativeModel(model_name)
        prompt = f"""
Update this 7-day workout plan based on the user's feedback.

ORIGINAL PLAN:
{original_plan}

USER FEEDBACK:
{feedback}

Return a complete revised 7-day plan. Preserve useful structure, clearly label Day 1–Day 7,
and make only sensible, general fitness changes. Do not diagnose medical conditions.
"""
        response = model.generate_content(prompt)
        return response.text if getattr(response, "text", None) else fallback
    except Exception:
        return fallback
