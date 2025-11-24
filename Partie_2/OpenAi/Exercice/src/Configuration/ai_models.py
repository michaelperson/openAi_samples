# --- ai_models.py ---
import openai
import os
from Configuration.config import config
from dotenv import load_dotenv
import time
import logging
class AIFactory: 
    """Factory centralisée pour tous les modèles IA du projet."""  
    
    def __init__(self):         
        load_dotenv()
        self.config = config
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  
        self.logger = logging.getLogger(__name__)  
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('app.log', mode='w')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def get_code_reviewer_response(self, user_content): 
        """Retourne une réponse d'un expert Python."""
        role =  "Tu es un code reviewer senior. Tu analyses le code pour:  - Bugs potentiels et edge cases  - Performance et optimisations - Lisibilité et maintenabilité - Sécurité et bonnes pratiques"

        return self._create_response(role, user_content)  

    def get_doc_writer_response(self, user_content): 
        role = "Tu es un technical writer expert. Tu rédiges des  documentations claires, concises et complètes au format Markdown."  
        return self._create_response(role, user_content)  
    
    def get_test_generator_response(self, user_content): 
        role = "Tu es expert en tests unitaires Python avec pytest.  Tu génères des tests complets avec fixtures, mocks et edge cases."  
        return self._create_response(role, user_content)  
    
    def get_python_expert_response(self, user_content):
        """Retourne une réponse d'un expert Python."""
        role = "Tu es un développeur Python senior avec 10+ ans d'expérience. Tu es expert en clean code, design patterns, et documentation. Tu fournis toujours des exemples concrets et des explications claires."
             
        return self._create_response(role, user_content)  


    def get_git_expert_response(self, user_content):
        """Retourne une réponse d'un expert Git."""
        role = "Tu es un expert Git et des bonnes pratiques de versioning. Tu maîtrises Conventional Commits et les workflows Git avancés. Tu rédiges des messages de commit clairs et descriptifs." 
             
        return self._create_response(role, user_content)    

    
    def get_Assitant_technique_response(self, user_content):
        """Retourne une réponse d'un Assitant technique formel."""
        role = "Tu es un assitant technique formel. Tu fournis des réponses précises, concises et professionnelles aux questions techniques posées." 
             
        return self._create_response(role, user_content) 

    
    def get_Tuteur_pedagogique_patient_response(self, user_content):
        """Retourne une réponse d'un tuteur pédagogique patient."""
        role = "Tu es un tuteur pédagogique patient. Tu expliques les concepts techniques de manière claire et accessible, en prenant le temps de détailler chaque étape pour faciliter la compréhension."
             
        return self._create_response(role, user_content)   

    
    def get_Expert_En_code_response(self, user_content):
        """Retourne une réponse d'un expert en code."""
        role = "Tu es un expert en code qui répond de manière concice et précise aux questions de code posées."
             
        return self._create_response(role, user_content)   
    
    
    def _create_response(self, role, user_content): 
        start = time.time()    
        try:
            messages = [ {"role": "system", "content": role}, {"role": "user", "content": user_content} ]  
            response = self.client.chat.completions.create( model=self.config['model'] , messages=messages, temperature=self.config['temperature']   )  
            
            duration = time.time() - start                 
            self.logger.info(f"Success in {duration:.2f}s")      
            return response.choices[0].message.content
        except Exception as e:
            duration = time.time() - start            
            self.logger.error(f"Failed in {duration:.2f}s: {e}")            
            raise 
    