#Installation package
#pip install openai

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
ApiKey = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=ApiKey)
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Explique les APIs"}]
)
print(response.choices[0].message.content)

