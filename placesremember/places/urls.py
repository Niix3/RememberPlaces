from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name="home"), #http://127.0.0.1:8000/
    path('reg/',views.registration,name="registration"),
    path('about/',views.about,name="about"),
    path('usrpage/',views.usrpage,name="usrpage"),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('social-auth/',
     include('social_django.urls', namespace='social')),
]