from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "WOMbasic"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-details'),
    path('submit/', views.SubmitRecipe.as_view(), name='submit'),
    path('recipe/<int:pk>/delete/', views.DeleteRecipe.as_view(), name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
