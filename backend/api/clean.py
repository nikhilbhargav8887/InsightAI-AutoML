from fastapi import APIRouter
import os

from backend.services.cleaning_service import clean_dataset

router = APIRouter()


@router.post("/clean/{filename}")
def clean(filename: str):

    file_path = os.path.join(
        "datasets",
        filename
    )

    cleaned_df, report = clean_dataset(
        file_path
    )

    output_file = os.path.join(
        "datasets",
        f"cleaned_{filename}"
    )

    cleaned_df.to_csv(
        output_file,
        index=False
    )

    return {
        "report": report,
        "cleaned_file": output_file
    }