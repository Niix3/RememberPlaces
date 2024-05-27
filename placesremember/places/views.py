from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm,UserRegistrationForm
from .models import locations
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


def usrpage(request,user_id):
    user = User.objects.get(id=user_id)
    mymodels = locations.objects.filter(user_owner=user)
    data = {'title':"Моя страница",'write_username':True, 'user': user, 'mymodels': mymodels}
    return render(request,'places/usrpage.html',context=data)



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('usrpage',user.id)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'places/login.html', {'title':'Вход в аккаунт','form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request,
        'places/reg.html',
        {'user_form': user_form})


def logout_view(request):
    logout(request)
    return redirect('home')
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!!!</h1>")