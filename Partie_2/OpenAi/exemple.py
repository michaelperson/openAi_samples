import openai  
import os
from dotenv import load_dotenv

load_dotenv()
ApiKey = os.getenv('OPENAI_API_KEY')
# On définit le rôle une seule fois
SYSTEM_ROLE = """Tu es un développeur Python senior, expert en clean code et en documentation."""
# Fonction qui encapsule la logique de messages
def create_messages(user_content):    
    return [  {"role": "system", "content": SYSTEM_ROLE}, 
              {"role": "user", "content": user_content}    ]
# Le client OpenAI
client = openai.OpenAI()
# L'appel est 100% dédié à la TÂCHE
response = client.chat.completions.create(   
     model="gpt-4",   
     messages=create_messages("Rédige une docstring au format docstring pour ce code: ..."))
print(response.choices[0].message.content)






