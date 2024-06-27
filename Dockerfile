FROM python:3.9-slim

WORKDIR /app

COPY ./sm2/requirements.txt .

#RUN pip install --no-cache-dir -r requirements.txt

COPY ./sm2 .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=sm2.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
