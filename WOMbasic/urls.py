from django.urls import path

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "WOMbasic"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-details'),
    path('submit/', views.SubmitRecipe.as_view(), name='submit'),
    path('recipe/<int:pk>/delete/', views.DeleteRecipe.as_view(), name='delete'),
    path('results/', views.search_results, name='search-results'),
    path('prof/<str:username>/', views.Profile.as_view(), name='prof'),
    path('forksubmit/<int:pk1>/', views.fork_recipe, name='fork-submit'),
    path('like/<int:pk>', views.LikeView, name='like_recipe'),
    path('recipe/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
