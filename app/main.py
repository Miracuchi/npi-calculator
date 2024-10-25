# app/main.py
from fastapi import FastAPI, Request
from .config import settings
from .routes.post.calculate import router as main_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE
)

@app.get("/")
async def root():
    return {"message": "Bienvenue sur mon API! Hello World Megatronoid"}


app.include_router(main_router)