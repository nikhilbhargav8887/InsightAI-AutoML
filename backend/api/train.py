from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.training_service import TrainingService

router = APIRouter()


class TrainRequest(BaseModel):
    file_path: str
    target_column: str


@router.post("/train")
def train_model(request: TrainRequest):

    service = TrainingService()

    return service.train(
        request.file_path,
        request.target_column
    )