from langchain_community.tools import TavilySearchResults
from langchain_openai import ChatOpenAI

web_search = TavilySearchResults(max_results=5)

llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools = [web_search])

def search_wiht_tavily(query: str) -> list[str]:
    return web_search.invoke(query)

def search_with_agent(query: str) -> list[str]:
    """
    LLM 이 Tavily 도구를 사용할지 말지 구분하며 응답합니다.
    :param query: 쿼리
    """
    
    ai_msg = llm_with_tools.invoke(query)
    
    tool_call = ai_msg.tool_calls[0]
    
    return web_search.invoke(tool_call["args"])