# app\routes\get\download_get.py
from fastapi import APIRouter

from app.models.users_model import UserDownload
from ...services.download_results import download_results

router = APIRouter()


@router.get("/download_results/")
async def download_results_route(user: UserDownload):
    return await download_results(user)