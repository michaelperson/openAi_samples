
# 1. Initialisation
import os 
from dotenv import load_dotenv 
from Embedding_Manager import EmbeddingManager

load_dotenv()
manager = EmbeddingManager(os.getenv("OPENAI_API_KEY"))

# 2. Création des embeddings pour les documents (Phase d'Indexation)
doc1_text = "Python est un langage de programmation polyvalent et populaire."
doc2_text = "Les chats sont de petits mammifères carnivores domestiqués."
doc3_text = "Le machine learning utilise Python pour l'analyse de données."

vector1 = manager.create_embedding(doc1_text)
vector2 = manager.create_embedding(doc2_text)
vector3 = manager.create_embedding(doc3_text)

# Simulation d'une base de données indexée
indexed_db = [
    {"text": doc1_text, "vector": vector1},
    {"text": doc2_text, "vector": vector2},
    {"text": doc3_text, "vector": vector3},
]

print("\n--- Indexation Terminée ---")
print(f"Taille du vecteur (ex): {len(vector1)}")

# 3. Requête et Recherche de Similarité (Phase de Retrieval)
query_text = "Quel est le meilleur langage pour la data science ?"

# Utilisation de la méthode de recherche pour trouver le meilleur document
best_match_result = manager.find_best_match(query_text, indexed_db)

if best_match_result:
    print(f"\nRequête: '{query_text}'")
    print("\n Meilleur Match trouvé:")
    print(f"  Document: '{best_match_result['text']}'")
    print(f"  Score de Similarité Cosinus: {best_match_result['similarity_score']:.4f}")

    # Pour comparaison, calculons la similarité directement entre la requête et le doc sur les chats (faible)
    query_vector = manager.create_embedding(query_text)
    similarity_with_cat = manager.calculate_cosine_similarity(query_vector, vector2)
    print(f"\n Similarité avec le document sur les chats: {similarity_with_cat:.4f}")