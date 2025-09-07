FROM python:3.11-slim

WORKDIR /app

RUN pip install fastapi uvicorn qdrant-client openai toml

COPY . . 

EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
