from sentence_transformers import SentenceTransformer
import numpy as np
from fastapi import FastAPI
from typing import Dict
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

@app.post("/")
async def similarity(inputs: Dict):
    reference = inputs["reference"]
    titles = inputs["other"]
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    reference_embedding = model.encode(reference)
    titles_embeddings = [model.encode(title) for title in titles]
    similarity_scores = [cosine_similarity(reference_embedding, title_embedding) for title_embedding in titles_embeddings]
    most_similar_title = titles[np.argmax(similarity_scores)]
    return {"top_result": most_similar_title}
