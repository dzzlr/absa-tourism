FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install scikit-learn scipy numpy xgboost
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]