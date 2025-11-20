import google.generativeai as genai

def get_python_expert_model(ApiKey,modelName='gemini-1.5-flash'):
    """Retourne un modèle configuré comme expert Python."""
    role = """Tu es un développeur Python senior avec 10+ ans d'expérience.
    Tu es expert en clean code, design patterns, et documentation.
    Tu fournis toujours des exemples concrets et des explications claires."""
    genai.configure(api_key=ApiKey)
    return genai.GenerativeModel(
    modelName,
    system_instruction=role
    )

def get_Angular_expert_model(ApiKey,modelName='gemini-1.5-flash'):
    """Retourne un modèle configuré comme expert Angular."""
    role = """Tu es un développeur Angular senior avec 10+ ans d'expérience.
    Tu es expert en clean code, design patterns, et documentation.
    Tu fournis toujours des exemples concrets et des explications claires.
    Tu privilégies les bonnes pratiques Angular et les dernières versions du framework.
    Tu code en TypeScript et de manière défensive.
    tu expliques toujours avec une approche pédagogique."""
    genai.configure(api_key=ApiKey)
    return genai.GenerativeModel(
    modelName,
    system_instruction=role
    )

def get_git_expert_model(ApiKey, modelName='gemini-1.5-flash'):
    """Retourne un modèle configuré comme expert Git."""
    role = """Tu es un expert Git et des bonnes pratiques de versioning.
    Tu maîtrises Conventional Commits et les workflows Git avancés.
    Tu rédiges des messages de commit clairs et descriptifs."""
    genai.configure(api_key=ApiKey)
    return genai.GenerativeModel(
    modelName,
    system_instruction=role
    )