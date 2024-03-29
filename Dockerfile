FROM python:alpine

COPY . .

RUN pip install pipenv && pipenv install --system --deploy

WORKDIR /app

ENV SETUP=CLOUD

CMD ["pipenv", "run", "gunicorn", "server:APP", "-b", "0.0.0.0:8080", "-w", "2"]
