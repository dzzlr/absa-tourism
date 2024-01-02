from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .routes import news_title, tourism_review

app = FastAPI(
    title="Text Classification Playground Model API",
    description="A simple API that use NLP model to predict",
    version="0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_title.router)
app.include_router(tourism_review.router)

@app.get("/")
async def index():
    return JSONResponse(
        status_code = status.HTTP_200_OK, 
        content = {
            "code":200, 
            "message": "Welcome to API Inference Playground of Text Classification"
        })