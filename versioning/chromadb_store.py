# versioning/chromadb_store.py

import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB with default settings
client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

embedding_fn = embedding_functions.DefaultEmbeddingFunction()

def save_version(text):
    import uuid
    doc_id = str(uuid.uuid4())

    collection.add(
        documents=[text],
        metadatas=[{"source": "chapter_1", "version": doc_id}],
        ids=[doc_id]
    )

    print(f"📚 Saved version with ID: {doc_id}")


def search_versions(query: str):
    print(f"\n🔍 Searching for similar versions to: \"{query}\"")
    results = collection.query(query_texts=[query], n_results=1)

    if not results['documents'] or not results['documents'][0]:
        print("No similar versions found.")
        return

    print("\n✅ Most relevant saved version:\n")
    print(results['documents'][0][0][:1000] + "...\n")  # Show top 1000 chars
    print(f"\n📎 Metadata: {results['metadatas'][0][0]}")
