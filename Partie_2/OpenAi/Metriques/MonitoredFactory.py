import time
import logging
import openai  
import os
from dotenv import load_dotenv

load_dotenv()

class MonitoredAIFactory:    
    def __init__(self):         
        self.client = openai.OpenAI(os.getenv('OPENAI_API_KEY'))        
        self.logger = logging.getLogger(__name__)        
        
    def _create_monitored_response(self, role, user_content, expert_name):        
        start = time.time()                
        try:            
            messages = [  {"role": "system", "content": role}, 
                          {"role": "user", "content": user_content}            
                       ]
            response = self.client.chat.completions.create(
                                model="gpt-4",                
                                messages=messages            )
            duration = time.time() - start            
            self.logger.info(f"{expert_name} - Success in {duration:.2f}s")                        
            return response.choices[0].message.content                    
        except Exception as e:            
            duration = time.time() - start            
            self.logger.error(f"{expert_name} - Failed in {duration:.2f}s: {e}")            
            raise        
    
    def get_python_expert_response(self, user_content):        
        role = "Tu es un développeur Python senior..."        
        return self._create_monitored_response(role, user_content, "python_expert")
    



    
