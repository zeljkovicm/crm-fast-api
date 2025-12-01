'''
    The idea behind having config.py is to have one central place for tunning the application.
        For example:
            Instead of having everywhere in code:
                os.getenv("DATABASE_URL")
                os.getenv("SECRET_KEY")
                os.getenv("JWT_EXPIRE")

        All that is needed to be done is:
            from app.core.config import settings

            settings.db.db_host
            settings.db.db_user
            settings.db.db_password

        Or for JWT:
            settings.jwt.jwt_secret_key
            settings.jwt_jwt_access_expirtaion_minutes

    This is basically the "brain" that is reading .env file and offers nice objects with those values.
'''


from pydantic.v1 import BaseSettings


class DBSettings(BaseSettings):
    '''
        BaseSettings is special Pydantic class that works as BaseModel,
        but it is able to automatically read values from .env file.
        Also, it does automatic type validation (int, str, etc...) and uses default values if those
        cannot be found in .env file.
        DBSettings class is inheriting BaseSettings.
    '''
    db_scheme: str = "postgresql+psycopg"
    db_host: str = "localhost"
    db_port: str = 5432
    db_user: str = "postgres"
    db_password: str = "root"
    db_name: str = "crm"

    class Config:
        '''
            Class Config - basically says 'when DBSettings is created read .env file'
        '''
        env_file = ".env"

    def database_uri(self) -> str:
        '''
            SQLAlchemy and Alembic are expecting one connection string, for example: 
                postgresql+psycopg://user:password@host:port/db_name

            For example that could be done with f string: 
                f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db_name}"

            Here, PostgresDsn.build is a Pydantic helper that connects URL from pieces and check wheter is valid.
        '''
        return (
            f"{self.db_scheme}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        )


class JWTSettings(BaseSettings):
    '''
        Inherits BaseSettings and same as DBSettings, it reads the .env file and takes these values if they exist
    '''
    jwt_secret_key: str = "CHANGE_THIS_KEY"
    jwt_algorithm: str = "HS256"
    jwt_access_expirtaion_minutes: int = 60

    class Config:
        env_file = ".env"


class AppSettings:
    '''
        Helper class with two objects, that represent all configurables that application uses:
            db - type DBSettings
            jwt - type JWTSettings
    '''
    db: DBSettings = DBSettings()
    jwt: JWTSettings = JWTSettings()


settings = AppSettings()
