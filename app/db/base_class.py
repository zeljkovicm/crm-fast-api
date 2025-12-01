from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    '''
        Base class for all future ORM models.
        This class is supposed to be inherited by all ORM models.
        In case there is a need with common columns, like:
            - id
            - created_at
            - updated_at

        These can be added here as fields that will be inherited by all other models
    '''
    pass
