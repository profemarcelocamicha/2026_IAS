# main.py
from fastapi import FastAPI
from app.services import hello

app = FastAPI()

@app.get("/")
def root():
    return {"message": hello()}
