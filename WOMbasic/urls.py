from django.urls import path

from . import views
from .views import HomeView

app_name = "WOMbasic"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-details'),
    path('submit/', views.insert, name='submit')
]