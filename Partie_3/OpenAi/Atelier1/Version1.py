from openai import OpenAI
from dotenv import load_dotenv
import os
import inspect

def setup_api(): 
    """Configure l'API OpenAI avec la clé depuis .env""" 
    load_dotenv() 
    api_key = os.environ.get("OPENAI_API_KEY") 
    if not api_key: 
        raise ValueError("OPENAI_API_KEY non trouvée dans .env") 
    return OpenAI(api_key=api_key)

def get_function_source(func): 
    """Récupère le code source d'une fonction""" 
    try: 
        return inspect.getsource(func) 
    except Exception as e: 
        raise ValueError(f"Impossible de récupérer le code source : {e}")
    
def generate_docstring(client, code): 
    """Génère une docstring via l'API OpenAI""" 
    prompt = f"""Tu es un développeur Python senior expert en documentation technique et en clean code.Ta mission est de rédiger une docstring complète et professionnelle au format Google Style pour la fonction Python ci-dessous.La docstring doit inclure :- Une description claire de ce que fait la fonction- La section Args avec chaque paramètre, son type et sa description- La section Returns avec le type de retour et sa description- La section Examples avec un exemple d'utilisation concretIMPORTANT : Ne renvoie QUE la docstring, sans balises markdown (pas de ```), sans commentaires additionnels, sans explication. La docstring doit être directement utilisable dans le code.Voici la fonction :{code}""" 
    
    try: 
        response = client.chat.completions.create( model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}] ) 
        return response.choices[0].message.content.strip() 
    except Exception as e: 
        print(f"Erreur API : {e}") 
        return None
    
def example_function(user_id, filters=None, include_metadata=False): 
    """Fonction d'exemple pour tester notre générateur""" 
    data = {"user_id": user_id, "data": [1, 2, 3]} 
    if filters: 
        # Applique les filtres pass 
        if include_metadata: data["metadata"] = {"created": "2024"} 
        return data

def main(): 
    client = setup_api()  
    try: 
        # Récupère le code source de notre fonction d'exemple 
        code = get_function_source(example_function) 
        print("Code source détecté :") 
        print(code) 
        print("\n" + "="*50 + "\n")  
        # Génère la docstring 
        docstring = generate_docstring(client, code)  
        if docstring: 
            print("Docstring générée :") 
            print(docstring) 
        else: 
            print("Erreur lors de la génération")  
    except Exception as e: 
        print(f"Erreur : {e}")
        
if __name__ == "__main__": 
    main()
