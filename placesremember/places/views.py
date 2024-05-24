from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def index(request): #HTTP request
    return HttpResponse("Страница приложения places")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!!!</h1>")