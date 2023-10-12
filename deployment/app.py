from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from process import send_to_endpoint
from utils.validator import Validator

app = FastAPI(
    title="Aspect-Based Sentiment Analysis of Tourist Review Model API",
    description="A simple API that use NLP model to predict the aspect class of tourist review",
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

@app.post("/predict-tourist-review")
async def predict_news(request: Request, response: Response):
    data = await request.json()
    validate = Validator(data['text'], 'required|min:20')

    if validate.getMessage()['code'] == 200:
        result = send_to_endpoint(validate.getMessage())
        return result

    elif validate.getMessage()['code'] == 400:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return validate.getMessage()
