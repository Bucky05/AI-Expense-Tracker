from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas
from app.database import SessionLocal
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: schemas.UserCreate):
    db = SessionLocal()
    try:
        db_user = db.query(models.User).filter(models.User.username == user.username).first()
    except Exception as e:
        print(e)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = get_password_hash(user.password)
    new_user = models.User(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(user: schemas.UserCreate):
    try:
        db = SessionLocal()
        db_user = db.query(models.User).filter(models.User.username == user.username).first()
        if not db_user or not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        token = create_access_token({"sub": db_user.username})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")
