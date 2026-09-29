import os
import google.generativeai as genai

def generate_nutrition_tip_with_flash(goal):
    demo = {
        "weight loss": "Prioritize balanced meals with vegetables, adequate protein, whole foods and water. Avoid extreme restriction.",
        "muscle gain": "Include a protein source in each meal and combine it with carbohydrates, vegetables and adequate hydration.",
        "general wellness": "Aim for balanced meals, regular hydration, enough sleep and a variety of fruits and vegetables.",
    }
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return demo.get(goal.lower(), demo["general wellness"])

    try:
        genai.configure(api_key=api_key)
        model_name = os.getenv("GEMINI_TIP_MODEL", "gemini-1.5-flash")
        model = genai.GenerativeModel(model_name)
        prompt = f"""
Give one concise, practical nutrition or recovery tip for a person whose fitness goal is: {goal}.
Keep it general, safe and easy to understand. Do not provide medical diagnosis or treatment.
"""
        response = model.generate_content(prompt)
        return response.text if getattr(response, "text", None) else demo.get(goal.lower(), demo["general wellness"])
    except Exception:
        return demo.get(goal.lower(), demo["general wellness"])
