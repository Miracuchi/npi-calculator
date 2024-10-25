# app\models\users.py
from ..db.connection import get_connection
from pydantic import BaseModel
from uuid import UUID

class Users(BaseModel):
    id: UUID
    username: str
    created_at: str
    
    @staticmethod # permet d'appeller la fonction sans l'instancier
    def create_user_table():
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE EXTENSION IF NOT EXISTS "pgcrypto";
                CREATE TABLE IF NOT EXISTS users (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    username TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
        conn.close()

class UserCreate(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    