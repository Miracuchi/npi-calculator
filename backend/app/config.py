from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME: str = "Mon API FastAPI"
    DEBUG_MODE: bool = True
    API_V1_STR: str = "/api/v1"
    
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432  # Valeur par défaut pour le port

    class Config:
        env_file = ".env"
        extra = "allow"
        

settings = Settings()

# Utilisation de la configuration de base de données
DB_CONFIG = {
    'dbname': settings.DB_NAME,
    'user': settings.DB_USER,
    'password': settings.DB_PASSWORD,
    'host': settings.DB_HOST,
    'port': settings.DB_PORT,
}
