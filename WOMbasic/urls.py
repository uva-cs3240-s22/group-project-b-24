from django.urls import path
from . import views
from .views import *
app_name = "WOMbasic"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-details'),
    path('image_upload', recipe_image_view, name = 'image_upload'),
    path('submit/', views.SubmitRecipe.as_view(), name='submit'),
    path('recipe/<int:pk>/delete/', views.DeleteRecipe.as_view(), name='delete')
]