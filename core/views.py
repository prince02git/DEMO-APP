import os
from django.http import JsonResponse


def index(request):
    return JsonResponse({
        "status": "running",
        "app": "demo-app",
        "environment": os.environ.get("ENVIRONMENT", "staging"),
    })


def health(request):
    return JsonResponse({"status": "healthy"}, status=200)
