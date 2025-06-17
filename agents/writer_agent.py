import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


def ai_writer_spin(raw_text: str) -> str:
    print("\n✍️ AI Writer (Gemini) is rewriting the content...")

    prompt = f"""Rewrite the following chapter with better flow and slight variation in sentence structure while preserving the original meaning:\n\n{raw_text}"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Error with Gemini Writer: {e}")
        return raw_text
