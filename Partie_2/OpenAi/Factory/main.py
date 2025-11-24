from ai_models  import get_python_expert_response, get_git_expert_response

# Besoin d'aide sur du code Python ?
response = get_python_expert_response("Explique comment fonctionnent les décorateurs Python")
print(response)

# Besoin d'un message de commit ?
response = get_git_expert_response("Rédige un commit message pour l'ajout d'une fonction de cache")
print(response)