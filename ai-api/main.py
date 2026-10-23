
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from matcher import MemberMatcher



app = FastAPI(
    title="AgriSoko Pocket G06 AI Service",
    description="Search group member profiles using TF-IDF and cosine similarity.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8081",
        "http://127.0.0.1:8081",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

matcher = MemberMatcher()


class SearchRequest(BaseModel):
    query: str = Field(
        min_length=1,
        max_length=500,
        description="A question or search term about a group member.",
    )


@app.get("/health")
def health():
    """Check whether the API is running."""
    return {
        "status": "healthy",
        "groupCode": matcher.group_code,
    }


@app.get("/model-info")
def model_info():
    """Describe the AI matching service."""
    return {
        "groupCode": matcher.group_code,
        "method": "TF-IDF with cosine similarity",
        "memberCount": len(matcher.members),
        "matchThreshold": 0.25,
        "version": "1.0.0",
    }


@app.post("/search")
def search_member(request: SearchRequest):
    """Find a possible member match."""
    query = request.query.strip()

    if not query:
        raise HTTPException(
            status_code=422,
            detail="The query must not be empty.",
        )

    return matcher.search(query)
