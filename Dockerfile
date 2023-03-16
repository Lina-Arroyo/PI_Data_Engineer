#Fase 4
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

RUN mkdir -p /app

COPY ./main.py /app

CMD ["uvicorn", "main:app --reload"]
