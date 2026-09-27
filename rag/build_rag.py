import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

DOCUMENT_FOLDER = "rag/documents"

documents = []
texts = []

for filename in os.listdir(DOCUMENT_FOLDER):
    if filename.endswith(".txt"):
        filepath = os.path.join(DOCUMENT_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        texts.append(text)
        documents.append(filename)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "rag/faiss_index.bin")

with open("rag/documents.pkl", "wb") as file:
    pickle.dump(documents, file)

with open("rag/texts.pkl", "wb") as file:
    pickle.dump(texts, file)

print("RAG index created successfully!")
print("Documents:", len(documents))