from fastapi import APIRouter

from app.api.v1 import auth

api_router = APIRouter()

api_router.include_router(auth.router)


'''
    Main router
    Collects all sub-routers (auth, customers, users) and exits as one API router, for example: 
        - api_router.include_router(customers.py)
        - api_router.include_router(meetings.py)
    
    In main.py is enoungh to import this package and to include this router to the main app router: 
        - from app.api.v1.api import api_router
        - app.include_router(api_router)
    
    Also, for future, I have added this one in v1 bundle, in case in future there is going to be some logic change.
'''
