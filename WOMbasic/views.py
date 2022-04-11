from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.http import HttpResponse
from .models import Ingredients, Recipe
from .forms import RecipeForm , IngredientsFormSet, IngredientsForm
from django.urls import reverse_lazy


class SubmitRecipe(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'WOMbasic/submit.html'
    #fields = '__all__'
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


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Recipe.objects.filter(recipe_name__contains=searched, recipe_description__contains=searched)
        return render(request, 'WOMbasic/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'WOMbasic/search_results.html', {})

def create_Ingredients(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredients.objects.filter(recipe=recipe)
    formset = IngredientsFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = recipe
            formset.save()
            return redirect('WOMbasic/submit.html', pk=recipe.id)

    context = {
        "formset": formset,
        "recipe": recipe,
        "ingredient": ingredients
    }

    return render(request, 'submit.html', context)

def create_ingredients_form(request):
    form = IngredientsForm()
    context = {
        "form": form
    }
    return render(request, "partials/ingredients_form.html", context)