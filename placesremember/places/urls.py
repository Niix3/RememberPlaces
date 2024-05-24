from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"), #http://127.0.0.1:8000/
    path('reg/',views.registration,name="registration"),
    path('about/',views.about,name="about"),
    path('usrpage/',views.usrpage,name="usrpage"),
]