# agents/writer_agent.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def ai_writer_spin(text: str) -> str:
    print("\n✍️ AI Writer (Gemini) is rewriting the content...")
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(
            f"Rewrite the following text for a smoother reading experience while preserving the original meaning:\n{text}"
        )
        return response.text
    except Exception as e:
        print("❌ Error with Gemini Writer:", e)
        return text
