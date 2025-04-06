from langchain_community.tools import TavilySearchResults

web_search = TavilySearchResults(max_results=5)

def search_wiht_tavily(query: str) -> list[str]:
    return web_search.invoke(query)