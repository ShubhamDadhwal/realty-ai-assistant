import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
listings = json.load(open("listings.json"))

texts = [f"{l['bhk']} BHK flat in {l['location']}, {l['price_lakh']} lakh, {l['description']}" for l in listings]
vectors = model.encode(texts, normalize_embeddings=True)

def retrieve(question, k=3):
    q = model.encode([question], normalize_embeddings=True)[0]
    scores = vectors @ q
    top = np.argsort(scores)[::-1][:k]
    return [texts[i] for i in top]

if __name__ == "__main__":
    for r in retrieve("2 BHK in Mohali under 50 lakh"):
        print(r)