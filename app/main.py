from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from .database import engine, Base
from .models import user as user_model
from app.routers import user

os.environ['PGCLIENTENCODING'] = 'UTF8'

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gestión de Usuarios",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS, que permite que q las peticiones invluyan cookis y tokens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)

@app.get("/", tags=["Root"])
def root():
    """Endpoint raíz de la API"""
    return {
        "message": "Gestión de Usuarios",
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
