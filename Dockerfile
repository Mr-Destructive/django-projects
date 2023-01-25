FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y redis-server

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "redis-server & daphne destructive_projects.asgi:application -b 0.0.0.0"]
