# from .connection import get_connection

# def create_user_table():
#     conn = get_connection()
#     with conn.cursor() as cursor:
#         cursor.execute("""
#             CREATE EXTENSION IF NOT EXISTS "pgcrypto";
#             CREATE TABLE IF NOT EXISTS users (
#                 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
#                 username TEXT NOT NULL,
#                 created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
#             )
#         """)
#         conn.commit()
#     conn.close()
# app/services/user_service.py
from uuid import uuid4
from datetime import datetime
from app.db.connection import get_connection
from app.models.users_model import Users
class UserService:
    def __init__(self):
        self.users = []  # Une liste pour stocker les utilisateurs en mémoire

    def user_exists(self, username: str) -> bool:
        # Vérifiez si le nom d'utilisateur existe déjà dans la base de données
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
            count = cursor.fetchone()[0]
        return count > 0

    def create_user(self, username: str) -> Users:
        if self.user_exists(username):
            raise ValueError("L'utilisateur existe déjà")
        user_id = str(uuid4())
        created_at = datetime.now().isoformat()
        print("hello")
        # Enregistrement de l'utilisateur dans la base de données
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (id, username, created_at)
                VALUES (%s, %s, %s)
            """, (user_id, username, created_at))
            conn.commit()

        # Optionnel : Ajouter l'utilisateur à la liste en mémoire
        self.users.append(Users(id=user_id, username=username, created_at=created_at))

        return Users(id=user_id, username=username, created_at=created_at)

    def get_user(self, username: str) -> Users:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
            row = cursor.fetchone()
        
            if row:
            # Créer un objet Users à partir de la ligne récupérée
                return Users(id=row[0], username=row[1], created_at=row[2])
            else:
                return None  # Ou vous pouvez lever une exception si l'utilisateur n'est pas trouvé

        conn.close()
      
    def get_user_by_username(self, username: str) -> Users:
        conn = get_connection()
        with conn.cursor() as cursor:
           cursor.execute("SELECT id, username, created_at FROM users WHERE username = %s", (username,))
           row = cursor.fetchone()
           if row:
                return Users(id=row[0], username=row[1], created_at=row[2].isoformat() if isinstance(row[2], datetime) else row[2] )
           return print('NO')
        
    def authenticate_user(self, username:str) -> Users:
        user = self.get_user_by_username(username)
        if user is None:
            print('Id incorrect')
        return user