from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from ..tasks.tourism_review import ABSATourism
from ..utils.validator import Validator
from ..utils.response import json_result

router = APIRouter(
    # prefix="/items",
    # tags=["items"],
    # responses={404: {"description": "Not found"}},
)

@router.post("/predict-tourist-review")
async def predict_reviews(request: Request, response: Response):
    data = await request.json()
    validate = Validator(data['text'], 'required|min:20')

    if len(validate.getMessage()) == 0:
        predict = ABSATourism(data['text'])
        result = json_result(data['text'], predict.result)
        return {
            'code': 200,
            'status': 'OK',
            'data': result
        }
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'code': 400,
            'status': 'BAD_REQUEST',
            'errors': validate.getMessage()
        }