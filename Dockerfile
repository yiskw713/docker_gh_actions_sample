FROM python:3.10.1-buster

WORKDIR /app
COPY ./main.py ./main.py

CMD ["python", "main.py"]

