from fastapi import FastAPI
import os
from .database import engine, Base
from .models import user
os.environ['PGCLIENTENCODING'] = 'UTF8'

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola funciona"}

@app.get("/health")
def health():
    return {"status": "ok"}
