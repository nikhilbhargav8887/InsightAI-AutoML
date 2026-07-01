from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.database.models import Dataset

router = APIRouter()


@router.get("/datasets")
def get_datasets(db: Session = Depends(get_db)):

    datasets = db.query(Dataset).all()

    return datasets