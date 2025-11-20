import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
ROLE = "Tu es un expert python qui explique des concepts de programmation de manière claire et concise en alexandrin"


modelName = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")


prompt = """Explique le concept de la récursivité en programmation avec un exemple simple en Python."""

ApiKey = os.getenv('ApiKey')
genai.configure(api_key=ApiKey)
model = genai.GenerativeModel(
    modelName,
    system_instruction=ROLE
)
response = model.generate_content(prompt)
print(response.text)