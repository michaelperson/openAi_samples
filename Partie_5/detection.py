
def contains_credit_card(text):    
    # Détection de suites de 13-19 chiffres    
    pattern = r'\b\d{13,19}\b'   
    return bool(re.search(pattern, text))

def contains_phone(text):    
    patterns = [ r'\+33\s?\d{9}',  # Format international       
                 r'0\d{9}',  # Format national        
                 r'\d{2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}[\s.-]?\d{2}'    ]    
    return any(re.search(p, text) for p in patterns)


def validate_prompt_before_send(prompt):    
    checks = [ ("email", contains_email),
               ("phone", contains_phone),
               ("credit_card", contains_credit_card),        
               ("ip_address", contains_ip_address),    ]        
    for check_name, check_func in checks:        
        if check_func(prompt):            
            logger.warning(f"Prompt blocked: contains {check_name}")            
            raise SecurityException(f"Prompt contains PII: {check_name}")        
        return True