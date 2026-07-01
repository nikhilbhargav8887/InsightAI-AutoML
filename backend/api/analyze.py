from fastapi import APIRouter
import os

from backend.services.analysis_service import analyze_dataset

router = APIRouter()


@router.get("/analyze/{filename}")
def analyze(filename: str):

    file_path = os.path.join(
        "datasets",
        filename
    )

    result = analyze_dataset(file_path)

    return result