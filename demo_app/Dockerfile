FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . demo_app/
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "2", "demo_app.wsgi:application"]
