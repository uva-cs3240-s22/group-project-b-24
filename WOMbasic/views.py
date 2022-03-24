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


def listView(request):
    latest_recipe_list = Recipe.objects.order_by()
    context = {'latest_recipe_list': latest_recipe_list,}
    return render(request, 'WOMbasic/recipe.html', context)

class HomeView(ListView):
    model = Recipe
    template_name = 'WOMbasic/home.html'