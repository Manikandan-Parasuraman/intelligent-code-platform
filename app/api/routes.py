from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.code_service import generate_and_apply
from app.core.security import verify_api_key

router = APIRouter()


class Query(BaseModel):
    question: str


@router.post("/generate")
def generate(q: Query, _: str = Depends(verify_api_key)):
    return generate_and_apply(q.question)