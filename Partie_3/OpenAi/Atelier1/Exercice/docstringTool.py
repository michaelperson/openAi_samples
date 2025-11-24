import os
import ast
from dotenv import load_dotenv
from openai import OpenAI

# --- Configuration et API ---

def setup_api():
    """Configure l'API OpenAI avec la clé depuis .env"""
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("ERREUR: La variable OPENAI_API_KEY est introuvable dans le fichier .env")
    return OpenAI(api_key=api_key)

def generate_docstring(client, code_segment, style="Google"):
    """
    Génère une docstring via l'API OpenAI selon le style demandé.
    
    Args:
        client: Client OpenAI instancié.
        code_segment (str): Le code source de la fonction.
        style (str): Le format de docstring (Google, NumPy, reStructuredText).
    """
    
    # Mapping pour clarifier les attentes dans le prompt
    style_instructions = {
        "google": "au format Google Style (Sections: Args, Returns, Examples)",
        "numpy": "au format NumPy Style (Sections: Parameters, Returns, Examples)",
        "rst": "au format reStructuredText (Sphinx standard :param, :return, etc.)"
    }
    
    chosen_style = style_instructions.get(style.lower(), style_instructions["google"])

    prompt = f"""Tu es un développeur Python senior expert en documentation technique.
Ta mission est de rédiger une docstring complète {chosen_style} pour la fonction ci-dessous.

Règles strictes :
1. Ne renvoie QUE la docstring (délimitée par des triples guillemets).
2. Pas de markdown, pas de backticks (```).
3. La description doit être concise et professionnelle.

Voici la fonction :
{code_segment}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Erreur API OpenAI : {e}")
        return None

# --- Logique Principale ---

def process_python_file(file_path, dry_run=False, doc_style="google"):
    """
    Analyse le fichier et insère les docstrings.
    
    Args:
        file_path (str): Chemin du fichier.
        dry_run (bool): Si True, affiche uniquement les changements sans écrire.
        doc_style (str): Style de la documentation (google, numpy, rst).
    """
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier {file_path} n'existe pas.")
        return

    print(f"--- Analyse de : {file_path} (Style: {doc_style}) ---")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()
    
    source_code = "".join(source_lines)
    
    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(f"Erreur de syntaxe critique : {e}")
        return

    try:
        client = setup_api()
    except ValueError as e:
        print(e)
        return

    functions = [
        node for node in ast.walk(tree) 
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    
    if not functions:
        print("Aucune fonction détectée.")
        return

    insertions = []

    for func in functions:
        if ast.get_docstring(func):
            if dry_run:
                print(f"[SKIP] {func.name} possède déjà une docstring.")
            continue

        print(f"[{'DRY-RUN' if dry_run else 'GENERATE'}] Traitement de la fonction '{func.name}'...")
        
        func_segment = ast.get_source_segment(source_code, func)
        docstring = generate_docstring(client, func_segment, style=doc_style)
        
        if docstring:
            # Gestion de l'indentation
            def_line_idx = func.lineno - 1
            indentation = source_lines[def_line_idx][:func.col_offset + 4]
            
            formatted_docstring = []
            for line in docstring.split('\n'):
                formatted_docstring.append(indentation + line)
            
            final_doc_block = "\n".join(formatted_docstring) + "\n"

            if dry_run:
                # Affichage prévisualisation
                print(f"\n--- Prévisualisation pour '{func.name}' ---")
                print(final_doc_block.rstrip())
                print("-------------------------------------------\n")
            else:
                # Préparation de l'insertion réelle
                first_instruction_line = func.body[0].lineno - 1
                insertions.append((first_instruction_line, final_doc_block))

    if dry_run:
        print("Mode Dry-Run terminé. Aucun fichier n'a été modifié.")
        return

    # Application des changements (uniquement si pas dry-run)
    insertions.sort(key=lambda x: x[0], reverse=True)
    for line_idx, doc_block in insertions:
        source_lines.insert(line_idx, doc_block)

    base_name, ext = os.path.splitext(file_path)
    output_path = f"{base_name}_commented{ext}"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(source_lines)
    
    print(f"\nSuccès ! Fichier généré : {output_path}")


    import logging
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('api_calls.log'),logging.StreamHandler()])
    logger = logging.getLogger(__name__)

    def generate_docstring(client, code):    
        logger.info("Appel API pour docstring")    
        try:        
            response = client.chat.completions.create(...)        
            logger.info("Succès API")        
            return response.choices[0].message.content    
        except Exception as e:        
            logger.error(f"Échec API : {e}")        
            return None
