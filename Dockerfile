FROM python:3.6-jessie

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
