from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app -- this is the core of the API
app = FastAPI()

# Root endpoint  -confirms the API is running


@app.get("/")
def read_root():
    return {"Message": "FastAPI is working!"}

# Path parameter endpoint - name comes directly from the URL


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, welcome to your first API"}

# Define the shape of the data we expect to receive - text must be string


class Question(BaseModel):
    text: str

# POST endpoint - receives a question as JSON and returns it back
# This is the pattern the RAG /ask endpoint will use


@app.post("/ask")
def ask_question(question: Question):
    # question.text goes into the RAG pipeline, RAG finds relevant document chunks then returns answer + source citations
    return {"you_asked": question.text, "answer": "I will answer this soon"}
