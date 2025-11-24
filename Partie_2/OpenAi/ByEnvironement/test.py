from Configuration.ai_models  import AIFactory

# Test de validation
def test_system_message(): 
    factory = AIFactory()  
    #Demander au modèle de se décrire 
    response = factory.get_python_expert_response( "En une phrase, qui es-tu et quel est ton rôle ?" )  
    print(response) 
    
# Test de cohérence
def test_consistency(): 
    factory = AIFactory()  
    # Faire 3 requêtes similaires 
    prompts = [ "Explique les décorateurs", "Explique les générateurs",  "Explique les context managers" ]  
    for prompt in prompts: 
        response = factory.get_python_expert_response(prompt) 
        # Toutes les réponses devraient avoir le même style 
        print(f"\n{prompt}:\n{response[:200]}...")

if __name__ == "__main__":
    print("Test de validation :")
    test_system_message() 
    print("\nTest de cohérence :")
    test_consistency()




    