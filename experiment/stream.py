from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
ApiKey = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=ApiKey)

stream = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)

for event in stream:
    print(event)