import pdfplumber
import io
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from LangChain.pdf_to_json_response import Data

parser = PydanticOutputParser(pydantic_object=Data)

template = """
다음 이력서 내용을 읽고 아래 JSON 형식에 맞게 정리해 주세요.

이력서:
{text}

JSON 형식:
{format_instructions}
"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

chain = (
    {"text": RunnablePassthrough()} 
    | prompt 
    | llm 
    | parser
)

def pdf_to_json_agent(pdf_bytes: bytes):
    """
    PDF 를 JSON 으로 변환합니다.
    :param pdf_bytes: PDF 파일의 바이너리 데이터
    """
    # PDF 파일을 열고 텍스트 추출
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf_file:
        text = ""
        for page in pdf_file.pages:
            text += page.extract_text()

    # LangChain 체인 호출해서 JSON으로 변환
    result = chain.invoke(text)
    
    print("result", result)

    return result