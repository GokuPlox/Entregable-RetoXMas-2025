from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
from .database import engine, Base
from .models import user as user_model
from app.routers import user
from app.init_db import init_db

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.environ['PGCLIENTENCODING'] = 'UTF8'

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gestión de Usuarios",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Evento de inicio: cargar datos iniciales
@app.on_event("startup")
async def startup_event():
    """Cargar datos iniciales en la base de datos al iniciar la aplicación"""
    logger.info("Inicializando base de datos...")
    init_db()
    logger.info("Base de datos inicializada correctamente")

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
