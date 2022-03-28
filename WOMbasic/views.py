from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponse
from . models import Recipe
from django.urls import reverse_lazy
from .forms import *

class SubmitRecipe(CreateView):
    model = Recipe
    template_name = 'WOMbasic/submit.html'
    fields = '__all__'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'WOMbasic/recipe_details.html'

class HomeView(ListView):
    model = Recipe
    template_name = 'WOMbasic/home.html'

class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'WOMbasic/delete_recipe.html'
    success_url = reverse_lazy('WOMbasic:home')

def recipe_image_view(request):
  
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RecipeForm()
    return render(request, 'hotel_image_form.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')