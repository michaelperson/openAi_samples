
import pytest from app.security 
import anonymize_prompt, contains_email, contains_phoneclass 

TestAnonymization:    
def test_email_detection(self):        
    """Vérifie que les emails sont détectés"""        
    assert contains_email("Contact: john.doe@example.com")        
    assert not contains_email("No email here")        

def test_phone_detection(self):        
    """Vérifie que les téléphones français sont détectés"""        
    assert contains_phone("+33 6 12 34 56 78")        
    assert contains_phone("06 12 34 56 78")        
    assert not contains_phone("No phone here")        
    
def test_anonymization_emails(self):        
    """Vérifie que l'anonymisation remplace les emails"""        
    original = "User john.doe@example.com reported an issue"        
    anonymized = anonymize_prompt(original)        
    assert "john.doe@example.com" not in anonymized        
    assert "[EMAIL]" in anonymized        
    
def test_anonymization_phones(self):        
    """Vérifie que l'anonymisation remplace les téléphones"""        
    original = "Call me at +33 6 12 34 56 78"        
    anonymized = anonymize_prompt(original)        
    assert "+33 6 12 34 56 78" not in anonymized        
    assert "[PHONE]" in anonymized        

def test_prompt_validation_blocks_pii(self):        
    """Vérifie que les prompts avec PII sont bloqués"""         
    from app.security import validate_prompt_before_send, SecurityException               
    dangerous_prompt = "Process data for jean.dupont@client.com"       
    with pytest.raises(SecurityException):            
        validate_prompt_before_send(dangerous_prompt)        
        
def test_api_keys_not_in_logs(self):        
    """Vérifie qu'aucune clé API n'apparaît dans les logs"""        
    import os        
    from app.logger import logger                
    api_key = os.environ.get("OPENAI_API_KEY")                
    # Simuler un appel API loggé        
    logger.info("API call successful")                
    # Vérifier que la clé n'est pas dans les logs        
    with open("app.log", "r") as f:            
        log_content = f.read()            
        assert api_key not in log_content