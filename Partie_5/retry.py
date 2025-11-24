import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session_with_retry(): 
    session = requests.Session()  
    # Configuration du retry automatique 
    retry_strategy = Retry( total=3, # Nombre maximum de retries 
                            backoff_factor=1, # Délai entre retries : 1s, 2s, 4s 
                            status_forcelist=[429, 500, 502, 503, 504], # Codes HTTP à retry 
                            allowed_methods=["POST", "GET"] # Méthodes à retry 
                            )  
    adapter = HTTPAdapter(max_retries=retry_strategy) 
    session.mount("http://", adapter) 
    session.mount("https://", adapter)  
    return session

def call_api_with_retry(prompt): 
    session = create_session_with_retry()  
    try: 
        response = session.post( "https://api.openai.com/v1/chat/completions", 
                                json={"model": "gpt-4o", "messages": [{"role": "user", "content": prompt}]}, timeout=30 ) 
        response.raise_for_status() 
        return response.json()  
    except requests.exceptions.RetryError: 
        logger.error("Max retries exceeded") 
        raise 
    except requests.exceptions.Timeout: 
        logger.error("Request timeout after 30s") 
        raise




    