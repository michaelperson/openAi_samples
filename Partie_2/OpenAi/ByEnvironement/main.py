from Configuration.ai_models  import AIFactory


factory = AIFactory()
# Besoin d'aide sur du code Python ?
response = factory.get_python_expert_response("Explique comment fonctionnent les décorateurs Python")
print(response)

# Besoin d'un message de commit ?
response = factory.get_git_expert_response("Rédige un commit message pour l'ajout d'une fonction de cache")
print(response)