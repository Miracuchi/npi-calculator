from fastapi import FastAPI, HTTPException, APIRouter, Query

from app.models.users_model import Users, UserCreate
from app.services.users_service import UserService


from fastapi import Body


router = APIRouter()



@router.post("/create_user/", response_model=Users)
async def create_user(user: UserCreate):
    user_service = UserService()  # Créer une instance de UserService
    return user_service.create_user(user.username)

