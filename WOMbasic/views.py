from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from . models import Recipe


def insert(request):
    try:
        sub_text = request.POST['nameOfRecipe']
    except KeyError:
        sub_text = "oopsies"
        return render(request, 'WOMbasic/submit.html')
    else:
        r = Recipe()
        r.recipe_name = request.POST['nameOfRecipe']
        r.save()
        return render(request, 'WOMbasic/recipe/list.html')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'WOMbasic/recipe_details.html'

class HomeView(ListView):
    model = Recipe
    template_name = 'WOMbasic/home.html'