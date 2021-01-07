from typing import List

from fastapi import Depends, FastAPI, HTTPException,APIRouter
from sqlalchemy.orm import Session
from common import oauth2_scheme
from . import userdao, models, schema
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


router=APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schema.User,tags=["users"])
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = userdao.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userdao.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schema.User],tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userdao.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schema.User,tags=["users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userdao.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=schema.Item,tags=["users"])
def create_item_for_user(
    user_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)
):
    return userdao.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[schema.Item],tags=["users"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = userdao.get_items(db, skip=skip, limit=limit)
    return items