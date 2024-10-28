from django.http import JsonResponse
from django.shortcuts import render

def index(request): 
  return render(request, "api/index.html")

def health_check(request):
  return JsonResponse({"status": "ok","message":"Server is Health"}, status=200)