FROM python:3.10

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

RUN apt-get update && apt-get install -y redis-server

CMD ["sh", "-c", "redis-server & daphne destructive_projects.asgi:application"]
