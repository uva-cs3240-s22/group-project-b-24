from django.urls import path

from . import views

app_name = "WOMbasic"
urlpatterns = [
    path('recipe/list', views.listView, name='listView'),
    path('recipe/', views.insert,name='submit'),
]