# main.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():    
   # Charger les variables d'environnement depuis .env    
      load_dotenv()        
   # Récupérer la clé de manière sécurisée    
      api_key = os.environ.get("ApiKey")        
      if not api_key:        
            raise ValueError("ApiKey non trouvée dans .env")        
   # Configurer le SDK    
      genai.configure(api_key=api_key)        
   # Instancier le modèle    
      model = genai.GenerativeModel('gemini-flash-latest')        
   # Faire l'appel    
      prompt = "Expliquez-moi les APIs d'IA en 3 phrases"    
      response = model.generate_content(prompt)        
    # Afficher la réponse    
      print(response.text)        
   # Bonus : afficher les tokens consommés    
      print(f"\nTokens utilisés : {response.usage_metadata.total_token_count}")

if __name__ == "__main__":    
     main()


