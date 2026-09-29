import os
import google.generativeai as genai

DEMO_PLAN = """7-DAY PERSONALIZED WORKOUT PLAN

Day 1 – Full Body
Warm-up: 5–10 minutes brisk walking and mobility.
Main workout:
- Bodyweight squats: 3 sets × 12 reps
- Incline push-ups: 3 × 10
- Glute bridges: 3 × 12
- Plank: 3 × 30 seconds
Cooldown: 5 minutes gentle stretching.

Day 2 – Cardio
Warm-up: 5–10 minutes.
Main workout:
- Brisk walk/jog intervals: 25 minutes
- Step-ups: 3 × 10 each leg
Cooldown: 5 minutes.

Day 3 – Upper Body
Warm-up: 5–10 minutes.
Main workout:
- Wall/incline push-ups: 3 × 10
- Resistance-band rows: 3 × 12
- Shoulder raises: 3 × 12
Cooldown: 5 minutes.

Day 4 – Recovery
Light walking for 20–30 minutes and gentle mobility.

Day 5 – Lower Body
Warm-up: 5–10 minutes.
Main workout:
- Squats: 3 × 12
- Reverse lunges: 3 × 8 each leg
- Calf raises: 3 × 15
Cooldown: 5 minutes.

Day 6 – Core + Cardio
Warm-up: 5–10 minutes.
Main workout:
- Marching/jogging: 15 minutes
- Dead bug: 3 × 10
- Plank: 3 × 30 seconds
Cooldown: 5 minutes.

Day 7 – Rest / Active Recovery
Easy walk, hydration and gentle stretching.

Safety note: Adjust exercises to your experience and stop if you experience pain or unusual symptoms.
"""


def generate_workout_gemini(name, age, weight, goal, intensity):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return DEMO_PLAN

    try:
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-1.5-pro")
        model = genai.GenerativeModel(model_name)
        prompt = f"""
Create a structured personalized 7-day workout plan for:
Name: {name}
Age: {age}
Weight: {weight} kg
Fitness goal: {goal}
Workout intensity: {intensity}

Requirements:
- Clearly label Day 1 through Day 7.
- Include warm-up (5–10 minutes), main workout, sets/reps or duration, and cooldown/recovery.
- Keep the plan practical and easy to follow.
- Adapt difficulty to the requested intensity.
- Do not claim to diagnose or treat medical conditions.
- Add a short safety note at the end.
"""
        response = model.generate_content(prompt)
        return response.text if getattr(response, "text", None) else DEMO_PLAN
    except Exception:
        return DEMO_PLAN
