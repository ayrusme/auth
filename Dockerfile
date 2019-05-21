FROM python:alpine

COPY . .

RUN pip install pipenv && pipenv install --system --deploy

WORKDIR /app

CMD ["gunicorn", "server:APP", "-b", "0.0.0.0:8080", "-w", "4"]
