from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.http import HttpResponse
from . models import Recipe
from . forms import RecipeForm, ForkForm
from django.urls import reverse_lazy


class Profile(ListView):
    model = Recipe
    template_name = 'WOMbasic/prof.html'

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


class ForkRecipe(CreateView):
    model = Recipe
    form_class = ForkForm
    template_name = 'WOMbasic/forksubmit.html'
    success_url = reverse_lazy('WOMbasic:home')


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Recipe.objects.filter(recipe_name__contains=searched)
        return render(request, 'WOMbasic/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'WOMbasic/search_results.html', {})

