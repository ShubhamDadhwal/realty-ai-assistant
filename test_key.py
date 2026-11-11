import os
from dotenv import load_dotenv
load_dotenv()
print("Key loaded:", os.getenv("GEMINI_API_KEY") is not None)