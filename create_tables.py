from dotenv import load_dotenv
import os

load_dotenv()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1324@localhost:5432/entregable_db")

try:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("Tabla 'users' creada correctamente")
except Exception as e:
    print(f"Error: {e}")
