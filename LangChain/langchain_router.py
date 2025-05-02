from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import UploadFile, File

from LangChain.search_agent import search_wiht_tavily, search_with_agent
from LangChain.today_search_agent import search_with_today_agent
from LangChain.pdf_to_json_agent import pdf_to_json_agent

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

@router.post("/search-agent-today")
async def search(body: message):
    """
    Agent 가 Tavily 도구를 사용할지 말지 구분하여 응답합니다.
    :body: 쿼리
    """
    return {"message": "Search results", "data": search_with_today_agent(body.message)}

@router.post("/pdf-to-json")
async def pdf_to_json(pdf: UploadFile = File(...)):
    """
    Agent 가 이력서 PDF 를 JSON 으로 변환합니다.
    :body: pdf
    """
    
    content = await pdf.read()
    return {"message": "results", "data": pdf_to_json_agent(content)}