from fastapi import APIRouter

from LangChain.search_agent import search_wiht_tavily

router = APIRouter()

@router.post("/search")
async def search(query: str):
    """
    Tavily 도구를 사용하여 검색합니다.
    :param query: 검색할 쿼리
    """
    return {"message": "Search results", "data": search_wiht_tavily(query)}