from fastapi import APIRouter, Depends

from app.models.users_model import UserOperation
from app.services.operations_service import OperationService
router = APIRouter()

@router.get("/user_operations/")
async def get_operations_of_user(user: UserOperation):
    
    operations = OperationService.operations_of_user(str(user.id))
    return {"user_id": user.id, "operations": [{"expression": op[0], "result": op[1]} for op in operations]}