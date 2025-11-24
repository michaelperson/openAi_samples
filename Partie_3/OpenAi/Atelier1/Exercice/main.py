import argparse
import sys
import os
from docstringTool import process_python_file

def main():
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(
        description="AI Docstring Generator - Ajoute automatiquement des docstrings à vos fichiers Python."
    )
    
    # Argument positionnel : le fichier
    parser.add_argument(
        "file", 
        help="Le chemin du fichier Python (.py) à documenter"
    )
    
    # Flag optionnel : Dry Run
    parser.add_argument(
        "--dry-run", 
        action="store_true", 
        help="Simule la génération et affiche les docstrings dans la console sans créer de fichier."
    )
    
    # Argument optionnel : Format
    parser.add_argument(
        "--format", 
        choices=["google", "numpy", "rst"], 
        default="google", 
        help="Le style de la docstring (défaut: google)"
    )

    # Analyse des arguments
    args = parser.parse_args()

    # Validation du fichier
    file_path = args.file.replace('"', '').replace("'", "") # Nettoyage simple
    
    if not file_path.endswith(".py"):
        print("Erreur : Le fichier cible doit avoir l'extension .py")
        sys.exit(1)
        
    # Appel du tool avec les arguments parsés
    process_python_file(
        file_path=file_path, 
        dry_run=args.dry_run, 
        doc_style=args.format
    )

if __name__ == "__main__":
    main()