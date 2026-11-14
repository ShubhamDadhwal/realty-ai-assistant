from fastapi import FastAPI
from pydantic import BaseModel
from rag import retrieve
from llm import ask_llm

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    docs = retrieve(q.question)
    prompt = (
        "Answer ONLY using the listings below. "
        "If the answer is not in them, say you don't know.\n\n"
        "Listings:\n" + "\n".join(f"- {d}" for d in docs) +
        f"\n\nQuestion: {q.question}"
    )
    return {"answer": ask_llm(prompt)}