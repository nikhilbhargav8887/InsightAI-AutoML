from fastapi import APIRouter, UploadFile, File, Form
import os

from backend.services.training_service import TrainingService

router = APIRouter()

UPLOAD_DIR = "datasets/raw"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/train")
async def train_model(
    file: UploadFile = File(...),
    target_column: str = Form(...)
):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = TrainingService().train(
        file_path=file_path,
        target_column=target_column
    )

    return result