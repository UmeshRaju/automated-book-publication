# retrieval/rl_search.py

import random
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

# Simulated reward model (mock reinforcement learning scoring)
def simulated_reward_score(text: str, query: str) -> float:
    score = 0
    score += text.lower().count(query.lower()) * 2
    score += random.uniform(0, 1)  # simulate variation
    return score


def rl_ranked_search(query: str, top_k=3):
    print(f"\n🔎 RL Ranking for query: '{query}'")

    results = collection.query(query_texts=[query], n_results=top_k)

    if not results['documents'] or not results['documents'][0]:
        print("❌ No documents found.")
        return

    candidates = zip(results['documents'][0], results['metadatas'][0])
    scored_candidates = []

    for doc, meta in candidates:
        score = simulated_reward_score(doc, query)
        scored_candidates.append((score, doc, meta))

    # Sort based on mock RL score
    ranked = sorted(scored_candidates, key=lambda x: x[0], reverse=True)

    print("\n🏆 Top RL-ranked document:")
    print(ranked[0][1][:1000] + "...\n")
    print(f"📎 Metadata: {ranked[0][2]} | 🎯 Score: {ranked[0][0]:.2f}")
