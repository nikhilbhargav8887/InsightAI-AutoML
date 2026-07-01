from fastapi import APIRouter

router = APIRouter()


@router.post("/train")
def train():

    return {
        "message": "Training endpoint is ready."
    }