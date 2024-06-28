FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["daphne", "-b", "0.0.0.0", "-p", "80", "sm2.asgi:application"]
