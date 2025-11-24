from openai import OpenAI
from dotenv import load_dotenv
import os
import subprocess

def setup_api(): 
    """Configure l'API OpenAI avec la clé depuis .env""" 
    load_dotenv() 
    api_key = os.environ.get("OPENAI_API_KEY") 
    if not api_key: 
        raise ValueError("OPENAI_API_KEY non trouvée dans .env") 
    return OpenAI(api_key=api_key)

def get_staged_diff(): 
    """Récupère le git diff des fichiers stagés""" 
    result = subprocess.run( ['git', 'diff', '--staged'], capture_output=True, text=True )  
    if result.returncode != 0: 
        raise RuntimeError("Erreur git diff: " + result.stderr)  
    if not result.stdout.strip(): 
        raise ValueError("Aucun fichier stagé (utilisez 'git add')")  
    return result.stdout

def generate_commit_message(client, diff): 
    """Génère un message de commit via l'API OpenAI""" 
    prompt = f"""Tu es un développeur senior expert en Git et Conventional Commits.Analyse ce git diff et rédige un message de commit au format : type(scope): descriptionTypes : feat, fix, docs, refactor, test, chore, styleNe renvoie QUE le message (une seule ligne), sans explication ni balises.Git diff :{diff}"""  
    try: 
        response = client.chat.completions.create( model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}] ) 
        return response.choices[0].message.content.strip() 
    except Exception as e: print(f"Erreur API : {e}") 
    return None

def main(): 
    client = setup_api()  
    try: 
        diff = get_staged_diff() 
        commit_message = generate_commit_message(client, diff)  
        if commit_message: 
            print("Message de commit suggéré :") 
            print(commit_message) 
            print(f'\nPour commiter : git commit -m "{commit_message}"') 
    except Exception as e: print(f"Erreur : {e}")
    
    if __name__ == "__main__": 
        main()
