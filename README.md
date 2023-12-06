# Aspect-Based Sentiment Analysis of Tourist Review

## Overview
This repository for modelling and deploying NLP Model especially on Text Classification. 

## NLP Tasks
### Aspect-Based Sentiment Analysis of Tourist Reviews using XGBoost
- The NLP Model provide 3 aspects of tourist review that are `['accessibility', 'facility', 'activity']`.
- The model has an accuracy 81%.
- XGBoost Model was created by [alfianmf](https://github.com/alfianmf)

### Text Classification of News Title using SVM
- The NLP Model provide 7 categories of news title that are `['finance', 'food', 'health', 'inet', 'oto', 'sport', 'travel']`.
- The model has an accuracy 85%.

## Requirements
- nltk 3.7
- pymongo 3.12.0
- fastapi 0.95.0
- uvicorn 0.21.1

## Running App
```bash
$ cd deployment
$ uvicorn app:app --reload
```

## Hitting API
```bash
$ curl -d '{"text":"Barusan dari situ dan pas ke toiletnya ampun kotor banget,dan bau pesing,tidak terawat padahal berbayar"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/predict-tourist-review
```

### Response Success
```json
{
    "code": 200,
    "status": "OK",
    "data": {
        "_id": "0642c431914b48879c40e589c4e3c6e9",
        "text": "Barusan dari situ dan pas ke toiletnya ampun kotor banget,dan bau pesing,tidak terawat padahal berbayar",
        "result": [
            {
                "label": "aksesibilitas",
                "score": {
                    "neutral": 0.997,
                    "positive": 0.001,
                    "negative": 0.002
                }
            },
            {
                "label": "fasilitas",
                "score": {
                    "neutral": 0.016,
                    "positive": 0.013,
                    "negative": 0.971
                }
            },
            {
                "label": "aktivitas",
                "score": {
                    "neutral": 0.549,
                    "positive": 0.098,
                    "negative": 0.353
                }
            }
        ],
        "createdAt": "2023-03-25T17:37:11.594742"
    }  
}
```

### Response Bad Request
```json
{
    "code": 400,
    "status": "BAD_REQUEST",
    "errors": [
        "must not be blank",
        "must be greater than or equal to 10 characters"
    ]
}
```
