# app/routes/main.py
from fastapi import FastAPI, HTTPException, APIRouter
from ...config import settings
from pydantic import BaseModel

router = APIRouter()

class Operation(BaseModel):
    expression: str

def evaluate_npi(expression: str):
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

@router.post("/calculate/")
async def calculate(operation: Operation):
    result = evaluate_npi(operation.expression)
    return {"result": result}

