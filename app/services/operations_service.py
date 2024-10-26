
from fastapi import HTTPException
from pydantic import BaseModel
from app.db.connection import get_connection

class OperationService(BaseModel):
    expression: str
    def save_operation(self, user_id, expression, result):
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO operations (user_id, expression, result)
                VALUES (%s, %s, %s)
            """, (str(user_id), expression, result))
            conn.commit()
        conn.close()

    def evaluate_npi(self, expression: str):
        stack = []
        tokens = expression.split()

        for token in tokens:
            # Vérifier si le token est un nombre (peut être négatif)
            try:
                # Convertir en float, cela gérera les nombres négatifs
                stack.append(float(token))
            except ValueError:
                # Sinon, c'est un opérateur
                try:
                    b = stack.pop()  # Deuxième opérande
                    a = stack.pop()  # Premier opérande
                except IndexError:
                    raise HTTPException(status_code=400, detail="Expression invalide.")
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise HTTPException(status_code=400, detail="Division par zéro non autorisée.")
                    stack.append(a / b)
                else:
                    raise HTTPException(status_code=400, detail="Opération non reconnue.")

        if len(stack) != 1:
            raise HTTPException(status_code=400, detail="Expression invalide.")

        return stack[0]
    
    @staticmethod
    def operations_of_user(user_id):
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT expression, result FROM operations WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
            result = cursor.fetchall()
        return result