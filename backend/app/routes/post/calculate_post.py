# app/routes/main.py
from fastapi import APIRouter

from app.models.users_model import UserOperation
from app.services.operations_service import OperationService 



router = APIRouter()



@router.post("/calculate/")
async def calculate(user: UserOperation, operation: OperationService):
    result = operation.evaluate_npi(operation.expression)
    operation.save_operation(user.id, str(operation.expression), result)
    return str(result) 
    
