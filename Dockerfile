FROM python:3.10-buster

WORKDIR /app/

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app/app
COPY ./static /app/static
COPY main.py /app/main.py

ENV __PYTHONPATH__=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
