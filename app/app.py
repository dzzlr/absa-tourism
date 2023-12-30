from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware

from routers import news_title, tourism_review

app = FastAPI(
    title="Text Classification Playground Model API",
    description="A simple API that use NLP model to predict",
    version="0.1",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_title.router)
app.include_router(tourism_review.router)

@app.get("/")
async def index():
    return {"message": "Welcome to API Inference Playground of Text Classification"}