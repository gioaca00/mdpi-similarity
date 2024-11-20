from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI(
    title="MDPI Similarity API",
    description="API to find the most similar title to a reference title",
)


class Titles(BaseModel):
    """Model for the input data"""

    reference: str
    other: list[str]


@app.get("/similarity")
def get_similarity():
    return {
        "message": "This endpoint only supports POST requests for similarity calculation."
    }


@app.post("/similarity")
def similarity(inputs: Titles):
    """Given a reference title and a list of other titles, return the most similar title to the reference one"""
    reference = inputs.reference
    titles = inputs.other

    model = SentenceTransformer("all-MiniLM-L12-v2")

    reference_embedding = model.encode(reference).reshape(1, -1)
    titles_embeddings = model.encode(titles)

    similarities = model.similarity(reference_embedding, titles_embeddings)

    top_result = titles[np.argmax(similarities)]

    return {"top_result": top_result}
