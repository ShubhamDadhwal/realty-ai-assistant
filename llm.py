import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(prompt):
    for attempt in range(4):
        try:
            response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
            return response.text
        except Exception as e:
            if attempt == 3:
                raise
            wait = 2 ** attempt
            print(f"LLM busy, retrying in {wait}s...")
            time.sleep(wait)

if __name__ == "__main__":
    print(ask_llm("Say hello in one short sentence."))