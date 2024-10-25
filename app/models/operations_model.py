from ..db.connection import get_connection
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Operation(BaseModel):
   id: UUID
   expression: str
   result: str
   created_at: datetime
   user_id: UUID
   
   @staticmethod
   def create_operations_table():
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE EXTENSION IF NOT EXISTS "pgcrypto";
                CREATE TABLE IF NOT EXISTS operations (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    expression TEXT NOT NULL,
                    result TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    user_id UUID NOT NULL REFERENCES users(id)
                )
            """)
            conn.commit()
        conn.close()