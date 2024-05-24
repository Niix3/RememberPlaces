from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.

def index(request): #HTTP request
    data = {
        'title':'Главная страница',
    }
    return render(request,'places/index.html',context=data)

def about(request):
    data = {'title':"О сайте"}
    return render(request,'places/about.html',context=data)

def registration(request):
    data = {'title': "Регистрация"}
    return render(request,'places/reg.html',context=data)

def usrpage(request):
    data = {'title':"Ваша страница"}
    return render(request,'places/index.html',context=data)
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!!!</h1>")