FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY main.py /app/main.py

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]
