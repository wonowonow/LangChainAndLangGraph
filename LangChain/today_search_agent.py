from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults
from langchain_core.runnables import RunnableConfig, chain

web_search = TavilySearchResults(max_results=3)

# Today
today = datetime.today().strftime('%Y-%m-%d')

# Prompt
prompt = ChatPromptTemplate([
    ("system", f"You are a helpful assistant that can search the web for information. Today date is {today}."),
    ("human", "{user_input}"),
    ("placeholder", "{message}"),
])

llm = ChatOpenAI(model="gpt-4o-mini")

# 도구 바인딩
llm_with_tools = llm.bind_tools(tools=[web_search])

# 체인 생성
llm_chain = prompt | llm_with_tools

@chain
def web_search_chain(user_input: str, config: RunnableConfig):
    input = {
        "user_input": user_input
    }
    ai_msg = llm_chain.invoke(input, config=config)
    print("ai_msg", ai_msg)
    tool_msgs = web_search.batch(ai_msg.tool_calls, config=config)
    print("tool_msgs", tool_msgs)
    return llm_chain.invoke({**input, "messages": [ai_msg, *tool_msgs]}, config=config)


def search_with_today_agent(query: str) -> list[str]:
    """
    Agent 가 Tavily 도구를 사용할지 말지 구분하여 응답합니다.
    :param query: 쿼리
    """
    
    # 체인 호출 실행
    return web_search_chain.invoke(query)