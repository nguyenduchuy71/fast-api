import models
import schemas
import utils
from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from database import engine, get_db
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash password
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/users/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with {id} not found')
    return user
