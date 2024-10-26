# app/main.py
from fastapi import FastAPI, Request

# from .db.operations import  create_operations_table
# from .db.users import create_user_table
from .config import settings
from .routes.post.calculate_post import router as main_router
from .routes.post.user_post import router as create_user
from .routes.get.user_get import router as login
from .routes.get.operation_get import router as get_operations_user
from .routes.get.download_get import router as download_results
from .models.operations_model import Operation
from .models.users_model import Users

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE
)

@app.on_event("startup")
async def startup_event():
    Users.create_user_table()
    Operation.create_operations_table()

@app.get("/")
async def root():
    return {"message": "Bienvenue sur mon API! Hello World Megatron"}


app.include_router(main_router)
app.include_router(login)
app.include_router(create_user)
app.include_router(get_operations_user)
app.include_router(download_results)