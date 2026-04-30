from fastapi import FastAPI
from main import run_pipeline

app = FastAPI()

@app.get("/analyze")
def analyze():
    result = run_pipeline()
    return result