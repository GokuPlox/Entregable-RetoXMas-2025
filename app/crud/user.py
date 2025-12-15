from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi import HTTPException, status
from app.utils.security import hash_password, verify_password
from typing import List, Optional

def create_user(db: Session, user: UserCreate):
    """Crear un nuevo usuario"""
    existing = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()

    if existing:
        if existing.username == user.username:
            raise HTTPException(400, "Username ya registrado")
        if existing.email == user.email:
            raise HTTPException(400, "Email ya registrado")
    
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username, 
        email=user.email, 
        password=hashed_password,
        is_active=True
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    """Autenticar usuario con username y password"""
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
        )
    if not verify_password(password, user.password):
        return False
    return user

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """Obtener usuario por username"""
    return db.query(User).filter(
        User.username == username, 
        User.is_active == True
    ).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """Obtener usuario por ID"""
    return db.query(User).filter(
        User.id == user_id,
        User.is_active == True
    ).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """Obtener lista de usuarios activos"""
    return db.query(User).filter(
        User.is_active == True
    ).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    """Actualizar información de usuario"""
    db_user = get_user_by_id(db, user_id)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    # Verificar si  username  existe
    if user_update.username and user_update.username != db_user.username:
        existing = db.query(User).filter(User.username == user_update.username).first()
        if existing:
            raise HTTPException(400, "Username ya registrado")
    
    # Verificar si email existe
    if user_update.email and user_update.email != db_user.email:
        existing = db.query(User).filter(User.email == user_update.email).first()
        if existing:
            raise HTTPException(400, "Email ya registrado")
    
    # Actualizar 
    if user_update.username:
        db_user.username = user_update.username
    if user_update.email:
        db_user.email = user_update.email
    if user_update.password:
        db_user.password = hash_password(user_update.password)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    db_user.is_active = False
    db.commit()
    return {"message": "Usuario eliminado exitosamente"}