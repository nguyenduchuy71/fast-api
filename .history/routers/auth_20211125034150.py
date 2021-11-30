from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from database import get_db
import schemas
router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(db: Session = Depends(get_db)):
    pass
