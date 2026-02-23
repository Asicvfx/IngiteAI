FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run migrations and collectstatic on startup? Or separate command?
# For Render, typically we use a build command and start command.
# Start command: gunicorn config.wsgi:application

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py create_superuser_auto && python manage.py cleanup_users && daphne -b 0.0.0.0 -p 8000 config.asgi:application"]
