from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponse
from . models import Recipe
from django.urls import reverse_lazy

class SubmitRecipe(CreateView):
    model = Recipe
    template_name = 'WOMbasic/submit.html'
    fields = '__all__'
    success_url = reverse_lazy('WOMbasic:home')

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
