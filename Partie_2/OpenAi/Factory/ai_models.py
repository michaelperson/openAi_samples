# --- Fichier: ai_models.py --- 
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration globale
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_python_expert_response(user_content):
   """Retourne une réponse d'un expert Python."""
   role = "Tu es un développeur Python senior avec 10+ ans d'expérience. Tu es expert en clean code, design patterns, et documentation. Tu fournis toujours des exemples concrets et des explications claires."
    
   messages = [{"role": "system", "content": role}, {"role": "user", "content": user_content}]
   response = client.chat.completions.create(model="gpt-4", messages=messages)
   return response.choices[0].message.content


def get_git_expert_response(user_content):
   """Retourne une réponse d'un expert Git."""
   role = "Tu es un expert Git et des bonnes pratiques de versioning. Tu maîtrises Conventional Commits et les workflows Git avancés. Tu rédiges des messages de commit clairs et descriptifs."
 
   messages = [{"role": "system", "content": role}, {"role": "user", "content": user_content}]
   response = client.chat.completions.create(model="gpt-4", messages=messages)
   return response.choices[0].message.content



