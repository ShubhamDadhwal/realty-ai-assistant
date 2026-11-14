# Realty Assistant
An AI chatbot that answers property questions (location, budget, BHK) using Retrieval-Augmented Generation (RAG).

## How it works
1. Property listings are converted into embeddings in advance.
2. A question arrives as JSON at the FastAPI `/ask` endpoint.
3. The question is converted into an embedding.
4. The closest listings are retrieved by similarity.
5. A prompt is built with those listings and the question.
6. The Gemini API answers using only those listings, and the answer is returned as JSON.

## Tech stack
Python, FastAPI, sentence-transformers, Gemini API

## Run locally
1. Create a virtual environment with Python 3.12 and install the packages.
2. Put `GEMINI_API_KEY=your_key` in a `.env` file.
3. Run `python -m uvicorn main:app --reload` and open `http://localhost:8000/docs`.

## Limitations and next steps
Vector search matches by similarity, not exact filters, so results can ignore budget or BHK. Next step: filter listings by location and budget before the vector search.