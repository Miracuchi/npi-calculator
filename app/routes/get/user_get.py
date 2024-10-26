from fastapi import  HTTPException, APIRouter

from app.models.users_model import Users, UserLogin
from app.services.users_service import UserService
from jose import jwt
import datetime
import os
from uuid import UUID
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")  # Changez ceci par une clé sécurisée
ALGORITHM = "HS256"  # Algorithme utilisé pour le jeton
EXPIRE_MINUTES = 30  # Durée d'expiration du jeton

router = APIRouter()

def create_jwt(user_id: UUID):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRE_MINUTES)
    to_encode = {"sub": str(user_id), "exp": expiration}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.get("/login/", response_model=Users)
async def login(user: UserLogin):
    user_service = UserService()

    authenticated_user = user_service.authenticate_user(user.username)

    if authenticated_user:
        token = create_jwt(authenticated_user.id)
        response = JSONResponse(content={"id": str(authenticated_user.id)})
        response.set_cookie(key="Authorization", value=token, httponly=True, secure=True)
        return response
    
    raise HTTPException(status_code=401, detail="Invalid credentials")
    # print("Welcome" + str(user.id))
    # return user