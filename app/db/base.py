from app.db.base_class import Base
from app.models.user import User

'''
    Centralised place where Alembic sees models.
    All models will be imported here later, for example: 
        from app.models.user import User
        from app.models.user import Customer
    This represent a list of all models that my database needs to have.
'''
