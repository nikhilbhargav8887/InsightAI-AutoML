from fastapi import APIRouter
from backend.services.ollama_service import OllamaService

router = APIRouter()


@router.post("/explain")
def explain(data: dict):

    explanation = OllamaService().explain(
        data["best_model"],
        data["metrics"]
    )

    return {
        "explanation": explanation
    }