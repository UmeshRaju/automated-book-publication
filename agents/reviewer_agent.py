# agents/reviewer_agent.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def ai_reviewer(text: str) -> str:
    print("\n🧐 AI Reviewer (Gemini) is improving clarity and coherence...")
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(
            f"Review and enhance the following text for clarity, grammar, and coherence without changing the original meaning:\n{text}"
        )
        return response.text
    except Exception as e:
        print("❌ Error with Gemini Reviewer:", e)
        return text
