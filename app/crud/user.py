from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from fastapi import HTTPException, status
from app.utils.security import hash_password

def create_user(db: Session, user: UserCreate):
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
        password=hashed_password
        )
    print(hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user