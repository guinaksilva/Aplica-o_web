from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import update
import app.models as models
import app.schemas as schemas

router = APIRouter(
    tags=["auth"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "teste@example.com": {
        "username": "teste@ceub.com",
        "full_name": "Teste",
        "email": "teste@example.com",
        "hashed_password": pwd_context.hash("123456"),
        "disabled": False,
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, email: str):
    user = db.get(email)
    if user:
        return user
    return None

def authenticate_user(fake_db, email: str, password: str):
    user = get_user(fake_db, email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "secret_key", algorithm="HS256")
    return encoded_jwt

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_pc(db: Session, pc_id: int):
    return db.query(models.PC).filter(models.PC.id == pc_id).first()

def get_pcs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PC).offset(skip).limit(limit).all()

def create_pc(db: Session, pc: schemas.PCCreate):
    db_pc = models.PC(**pc.dict())
    db.add(db_pc)
    db.commit()
    db.refresh(db_pc)
    return db_pc

def update_pc(db: Session, id: int, pc: schemas.PCUpdate):
    update_pc = update(models.PC).where(models.PC.id == id).values(
        name=pc.name,
        description=pc.description
    )
    db.execute(update_pc)
    db.commit()
    return update_pc


def delete_pc(db: Session, pc_id: int):
    db_pc = db.query(models.PC).filter(models.PC.id == pc_id).first()
    if db_pc:
        db.delete(db_pc)
        db.commit()
    return db_pc