import pickle
import faiss
from sentence_transformers import SentenceTransformer

index = faiss.read_index("rag/faiss_index.bin")

with open("rag/texts.pkl", "rb") as file:
    texts = pickle.load(file)

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "How can I manage my monthly spending?"

query_embedding = model.encode([query])

distances, results = index.search(query_embedding, k=2)

print("Query:", query)
print("\nRelevant Information:\n")

for result in results[0]:
    print(texts[result])
    print()