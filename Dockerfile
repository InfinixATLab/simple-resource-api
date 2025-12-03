FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn store_api.wsgi:application --bind 0.0.0.0:8000"]