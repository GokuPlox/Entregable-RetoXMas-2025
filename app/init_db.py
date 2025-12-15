"""
Script de inicialización de datos para la base de datos
Carga usuarios iniciales si la base de datos está vacía
"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password
from app.database import SessionLocal
import logging

logger = logging.getLogger(__name__)


INITIAL_USERS = [
    {
        "id": 1,
        "username": "Eli1",
        "email": "user@example.com",
        "password": "password123",  
        "is_active": True
    },
    {
        "id": 2,
        "username": "Eli3",
        "email": "user3@example.com",
        "password": "password123",
        "is_active": True
    },
    {
        "id": 3,
        "username": "string",
        "email": "user20@example.com",
        "password": "password123",
        "is_active": True
    },
    {
        "id": 4,
        "username": "Eli5",
        "email": "user5@example.com",
        "password": "password123",
        "is_active": True
    }
]

def init_db():
    """Inicializar la base de datos con datos por defecto"""
    db = SessionLocal()
    try:
       
        user_count = db.query(User).count()
        
        if user_count == 0:
            logger.info("Base de datos vacía. Cargando usuarios iniciales...")
            
            for user_data in INITIAL_USERS:
               
                hashed_password = hash_password(user_data["password"])
                
                
                db_user = User(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=hashed_password,
                    is_active=user_data["is_active"]
                )
                
                db.add(db_user)
                logger.info(f"✅ Usuario creado: {user_data['username']}")
            
            db.commit()
            logger.info(f" {len(INITIAL_USERS)} usuarios iniciales cargados correctamente")
        else:
            logger.info(f" Base de datos ya contiene {user_count} usuarios. No se cargan datos iniciales.")
    
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Configurar logging para pruebas directas
    logging.basicConfig(level=logging.INFO)
    init_db()
