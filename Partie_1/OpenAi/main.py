# main.py
import os
from dotenv import load_dotenv
from openai import OpenAI

def main():    
   # Charger les variables d'environnement depuis .env    
      load_dotenv()        
   # Récupérer la clé de manière sécurisée    
      api_key = os.environ.get("OPENAI_API_KEY")        
      if not api_key:        
            raise ValueError("OPENAI_API_KEY non trouvée dans .env")        
   # Configurer le SDK    
      client = OpenAI(api_key=api_key)    
    # Faire l'appel
      response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Expliquez-moi les APIs d'IA en 3 phrases"}
        ]
    )
    
    # Afficher la réponse
      print(response.choices[0].message.content)
    
    # Bonus : afficher les tokens consommés
      print(f"\nTokens utilisés : {response.usage.total_tokens}")

if __name__ == "__main__":    
     main()


