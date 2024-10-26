# app\services\download_results.py
import csv
import os

from app.services.users_service import UserService
from .operations_service import OperationService
from ..models.users_model import UserDownload
from fastapi.responses import FileResponse


async def download_results(user: UserDownload):
    operations = OperationService.operations_of_user(user.id)
    username = UserService.get_username_by_id(user.id)

    file_path = f"results_{str(username)}.csv"

    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Expression", "Result"])
        for op in operations:
            writer.writerow([op[0], op[1]])

    response = FileResponse(path=file_path, media_type='text/csv', filename=file_path)
    return response