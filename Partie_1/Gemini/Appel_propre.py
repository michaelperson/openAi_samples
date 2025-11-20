#Installation package
#pip install google-generativeai

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
ApiKey = os.getenv('ApiKey')
genai.configure(api_key=ApiKey)
model = genai.GenerativeModel('gemini-flash-latest')
response = model.generate_content("Explique les APIs")
print(response.text)