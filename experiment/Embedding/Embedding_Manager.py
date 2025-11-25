import openai
from openai import OpenAI
import numpy as np
from typing import List, Dict, Optional

class EmbeddingManager:
    """
    Gère la création d'embeddings de texte et le calcul de similarité cosinus.
    """

    # Modèle d'embedding recommandé par OpenAI
    EMBEDDING_MODEL = "text-embedding-3-small"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialise le client OpenAI.
        
        :param api_key: Votre clé API OpenAI (optionnel si définie dans l'environnement).
        """
        # Initialisation du client OpenAI
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = OpenAI() # Utilise la variable d'environnement OPENAI_API_KEY
            
        print(f"EmbeddingManager initialisé avec le modèle: {self.EMBEDDING_MODEL}")

    # --- Méthode Principale : Création d'Embedding ---
    def create_embedding(self, text: str) -> Optional[np.ndarray]:
        """
        Convertit une chaîne de texte en un vecteur d'embedding NumPy.

        :param text: Le texte à vectoriser.
        :return: Un vecteur NumPy (ndarray) ou None en cas d'erreur.
        """
        try:
            # L'API accepte une liste, même si c'est un seul élément
            response = self.client.embeddings.create(
                input=[text],
                model=self.EMBEDDING_MODEL
            )
            # Récupération du vecteur et conversion en tableau NumPy
            embedding_vector = np.array(response.data[0].embedding)
            return embedding_vector
            
        except openai.APIError as e:
            print(f"Erreur API lors de la création de l'embedding: {e}")
            return None
        except Exception as e:
            print(f"Une erreur inattendue est survenue: {e}")
            return None

    # --- Méthode Utile : Calcul de Similarité ---
    @staticmethod
    def calculate_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """
        Calcule la similarité cosinus entre deux vecteurs.
        Une valeur proche de 1.0 indique une forte similarité sémantique.

        :param vec_a: Le premier vecteur NumPy.
        :param vec_b: Le second vecteur NumPy.
        :return: Le score de similarité cosinus (float entre -1.0 et 1.0).
        """
        # La similarité cosinus peut être calculée comme le produit scalaire
        # si les vecteurs sont normalisés (ce qui est le cas pour les embeddings OpenAI)
        similarity = np.dot(vec_a, vec_b)
        
        # Pour des vecteurs non normalisés, on utiliserait :
        # similarity = np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))
        
        return float(similarity)

    # --- Méthode d'Exemple RAG (Simplifiée) ---
    def find_best_match(self, query: str, indexed_data: List[Dict[str, any]]) -> Optional[Dict[str, any]]:
        """
        Trouve le document le plus pertinent dans une base de données indexée.
        
        :param query: La requête utilisateur.
        :param indexed_data: Liste de dictionnaires contenant 'text' et 'vector'.
        :return: Le dictionnaire du meilleur match ou None.
        """
        query_vector = self.create_embedding(query)
        if query_vector is None:
            return None
        
        best_match = None
        max_similarity = -1.0
        
        for item in indexed_data:
            similarity = self.calculate_cosine_similarity(query_vector, item["vector"])
            
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = item
                best_match["similarity_score"] = max_similarity
                
        return best_match