import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


def ai_reviewer(text: str) -> str:
    print("\n🧐 AI Reviewer (Gemini) is improving clarity and coherence...")

    prompt = f"""Act as a grammar and style reviewer. Improve clarity, coherence, grammar, and word choice of the following passage:\n\n{text}"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Error with Gemini Reviewer: {e}")
        return text
