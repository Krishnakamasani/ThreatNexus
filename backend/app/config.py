from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url:str="postgresql+psycopg://threatnexus:password@localhost:5432/threatnexus"
    jwt_secret:str="change-me"
settings=Settings()
