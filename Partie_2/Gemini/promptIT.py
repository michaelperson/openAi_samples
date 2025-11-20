from Configuration.ai_models import get_python_expert_model, get_git_expert_model, get_Angular_expert_model
from dotenv import load_dotenv 
import os

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
modelName = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")


#Besoin d'aide pour un concept Python ?
prompt_python = """Explique le concept de la programmation orientée objet en Python avec un exemple simple."""
model_python = get_python_expert_model(api_key,modelName)

#besoin d'aide pour Git ?
prompt_git = """Explique le concept de branching et merging dans Git avec un exemple simple.""" 
model_git = get_git_expert_model(api_key,modelName)
#Besoin d'aide pour Angular ?
prompt_angular = """Explique le concept de data binding dans Angular avec un exemple simple."""
model_angular = get_Angular_expert_model(api_key,modelName)
def generate_content(model, prompt):
    response = model.generate_content(prompt)
    return response.text  
  
response_python = generate_content(model_python, prompt_python)
response_git = generate_content(model_git, prompt_git)
response_angular = generate_content(model_angular, prompt_angular)
print("Réponse Python :")
print(response_python)
print("\nRéponse Git :")
print(response_git)
print("\nRéponse Angular :")
print(response_angular)
print("\n")
print("Fin des exemples d'utilisation des modèles experts.")

