import re
def anonymize_prompt(prompt, user_data): 
    # Remplacement des données utilisateur 
    prompt = prompt.replace(user_data['name'], '[USER_NAME]') 
    prompt = prompt.replace(user_data['email'], '[USER_EMAIL]')  

    # Regex pour emails génériques 
    prompt = re.sub(r'[\w.+-]+@[\w-]+\.[\w.-]+', '[EMAIL]', prompt)  


    # Regex pour numéros de téléphone français 
    prompt = re.sub(r'\+33\s?\d{1}\s?\d{2}\s?\d{2}\s?\d{2}\s?\d{2}', '[PHONE]', prompt) 
    prompt = re.sub(r'0\d{1}\s?\d{2}\s?\d{2}\s?\d{2}\s?\d{2}', '[PHONE]', prompt)  




    # Adresses IP 
    prompt = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', '[IP_ADDRESS]', prompt)  

    
    # Numéros de carte bancaire (4 derniers chiffres visibles) 
    prompt = re.sub(r'\b\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\b', '[CARD_NUMBER]', prompt)  
    return prompt



