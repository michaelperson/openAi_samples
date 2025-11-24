import logging
import hashlib
from datetime import datetime

# Configuration du logger
logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                      handlers=[ logging.FileHandler('ai_api_calls.log'), logging.StreamHandler() ])
logger = logging.getLogger('ai_api')

def call_openai_api(prompt, user_id, operation_type): 
    start_time = datetime.now()  
    # Anonymisation du prompt (fonction définie précédemment) 
    anonymized_prompt = anonymize_prompt(prompt)  
    # Hash pour traçabilité 
    prompt_hash = hashlib.sha256(prompt.encode('utf-8')).hexdigest()  
    try: 
        # Appel API réel 
        response = client.chat.completions.create( model="gpt-4o", 
                                                   messages=[{"role": "user", "content": anonymized_prompt}] )  
        end_time = datetime.now() 
        duration_ms = (end_time - start_time).total_seconds() * 1000  
        # Estimation des tokens (à adapter selon l'API) 
        input_tokens = response.usage.prompt_tokens 
        output_tokens = response.usage.completion_tokens  
        # Log de succès (SANS le contenu du prompt ou de la réponse) 
        logger.info( f"API_SUCCESS | " f"user_id={user_id} | " f"operation={operation_type} | " f"model=gpt-4o | " f"prompt_hash={prompt_hash[:16]}... | " f"status=200 | " f"duration_ms={duration_ms:.2f} | " f"tokens_in={input_tokens} | " f"tokens_out={output_tokens}" )  
        
        return response.choices[0].message.content  
    except Exception as e: 
        end_time = datetime.now() 
        duration_ms = (end_time - start_time).total_seconds() * 1000  
        # Log d'erreur (SANS le contenu du prompt) 
        logger.error( f"API_ERROR | " f"user_id={user_id} | " f"operation={operation_type} | " f"model=gpt-4o | " f"prompt_hash={prompt_hash[:16]}... | " f"error_type={type(e).__name__} | " f"duration_ms={duration_ms:.2f}" )  
        raise



    
