import google.generativeai as genai
from dotenv import load_dotenv
from sample import calculate_totalRate
import os
import inspect

def setup_api():
# Récupération de la clé API depuis les variables d'environnement
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY non trouvée dans .env")
    genai.configure(api_key=api_key)
 

def generatePrompt(code_source):
    #Génère une docstring via l'API Gemini
    prompt = f"""Tu es un développeur Python senior expert en documentation technique.
    Ta mission est de rédiger une docstring au format Google Style pour cette fonction.
    Inclus : description, Args, Returns, Examples.
    Ne renvoie QUE la docstring, sans balises markdown ni commentaires.
    Voici le code source de la fonction :
    {code_source}
    """
    return prompt

def generate_docstring(prompt, model_name='gemini-flash-latest'):
   
    model = genai.GenerativeModel(model_name)
    try:        
        #Nombre de token qui seront utilisés
        modelName = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")
        total_tokens = model.count_tokens(prompt)
        print(f"Total tokens : {total_tokens}")
        response = model.generate_content(prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Candidates tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Total tokens: {response.usage_metadata.total_token_count}")
        return response.text
    except Exception as e:
        print(f"Erreur API : {e}")
        return None
    
def main():
    setup_api()
    code = inspect.getsource(calculate_totalRate)
    source = generatePrompt(code)    
    modelName = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")
    docstring = generate_docstring(source, modelName)
    if docstring:
        print("Docstring générée :")
        print("---------------------")
        print(docstring)
        print("---------------------")

if __name__ == "__main__":
 main()