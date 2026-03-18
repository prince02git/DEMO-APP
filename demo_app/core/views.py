import json
from django.http import JsonResponse


def root_view(request):
    return JsonResponse({"status": "running", "app": "demo-app", "environment": "staging"})


def health_view(request):
    return JsonResponse({"status": "healthy"}, status=200)
