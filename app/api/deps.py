from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db


def get_db_session(db: Session = Depends(get_db)) -> Session:
    return db


'''
    Dependencies that are used in multiple routes
    Theoretically, this is part of API layer that is responsible for cross-section things:
        - autentification
        - authorization
        - opening a connection to database
    
    The idea behind is not to repeat myself by writting the same code for reading token and user,
    but to use it as dependency: 
        - current_user: User = Depends(get_current_user)
'''
