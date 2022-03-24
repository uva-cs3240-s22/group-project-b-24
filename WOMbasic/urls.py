from django.urls import path

from . import views
from .views import HomeView

app_name = "WOMbasic"
urlpatterns = [
    path('recipe/list', views.listView, name='listView'),
    path('recipe/', views.insert, name='submit'),
    path('', views.HomeView.as_view(), name='home'),
]