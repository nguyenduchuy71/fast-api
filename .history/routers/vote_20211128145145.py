from fastapi import status, Response, HTTPException, Depends, APIRouter
from database import get_db
from sqlalchemy.orm.session import Session
import schemas
import models
import oauth2
router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    if vote.dir == 1:
        db.query(models.Vote).filter(models.Vote.post_id ==
                                     vote.post_id, models.Vote.user_id == current_user.id)
    
