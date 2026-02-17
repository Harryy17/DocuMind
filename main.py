import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import query_agent

app = FastAPI(title="Local Agentic RAG API")

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.get("/")
async def root():
    return {"status": "ok", "message": "Agentic RAG API is running."}

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    print(f"Received: {request.question}")
    result = query_agent(request.question)
    return QueryResponse(answer=result)

if __name__ == "__main__":
    # This host 0.0.0.0 is CORRECT for the server
    uvicorn.run(app, host="0.0.0.0", port=8000)