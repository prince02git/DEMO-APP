# demo-app

A minimal Django application with two endpoints.

## Endpoints

| Method | Path      | Response                                                        |
|--------|-----------|-----------------------------------------------------------------|
| GET    | `/`       | `{"status": "running", "app": "demo-app", "environment": "..."}` |
| GET    | `/health` | `{"status": "healthy"}`                                         |

## Running locally

```bash
cp .env.example .env
pip install -r requirements.txt
python manage.py runserver
```

## Running with Docker

```bash
docker build -t demo-app .
docker run -p 8080:8080 demo-app
```

## Environment variables

| Variable      | Default                              | Description                  |
|---------------|--------------------------------------|------------------------------|
| `SECRET_KEY`  | insecure default                     | Django secret key            |
| `DEBUG`       | `False`                              | Enable debug mode            |
| `ENVIRONMENT` | `staging`                            | Shown in `/` response        |
