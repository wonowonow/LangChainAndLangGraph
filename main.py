from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="LangChain & LangGraph API",
    description="FastAPI application to demonstrate LangChain and LangGraph capabilities",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importing the router from langchain_router.py
from LangChain import langchain_router

app.include_router(langchain_router.router, prefix= "/chain", tags=["LangChain"])


@app.get("/")
async def root():
    return {"message": "Welcome to the LangChain & LangGraph API!",
            "endpoints": {
            "LangChain": "/chain",
            "LangGraph": "/graph"
        }}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)