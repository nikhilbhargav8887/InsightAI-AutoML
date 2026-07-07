from fastapi import APIRouter
from backend.services.ollama_service import OllamaService

router = APIRouter()


@router.post("/chat")
def chat(data: dict):
    service = OllamaService()

    answer = service.chat(data)

    return {
        "answer": answer
    }