from fastapi import APIRouter
from pydantic import BaseModel

from LangChain.search_agent import search_wiht_tavily, search_with_agent

router = APIRouter()

class message(BaseModel):
    message: str

@router.post("/search")
async def search(body: message):
    """
    Tavily 도구를 사용하여 검색합니다.
    :body: 쿼리
    """
    return {"message": "Search results", "data": search_wiht_tavily(body.message)}

@router.post("/search-agent")
async def search(body: message):
    """
    Agent 가 Tavily 도구를 사용할지 말지 구분하여 응답합니다.
    :body: 쿼리
    """
    return {"message": "Search results", "data": search_with_agent(body.message)}