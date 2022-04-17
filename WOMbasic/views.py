from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.http import HttpResponse
from . models import Recipe, Profile
from . forms import RecipeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class Profile(ListView):
    model = Recipe
    template_name = 'WOMbasic/prof.html'

    def get_name(self):
        name = self.request.GET.get('username')
        return name

    def dispatch(self, request, *args, **kwargs):
        self. uname = kwargs.get('username', "any_default")
        return super(Profile, self).dispatch(request, *args, **kwargs)


class SubmitRecipe(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'WOMbasic/submit.html'
    #fields = '__all__'
    success_url = reverse_lazy('WOMbasic:home')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'WOMbasic/recipe_details.html'
    #profiles = Profile.objects.all()
    #context = {}
    #extra_context = {'profiles': Profile.objects.all()}


class HomeView(ListView):
    model = Recipe
    template_name = 'WOMbasic/home.html'
    #extra_context = {'profiles': Profile.objects.all()}


class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'WOMbasic/delete_recipe.html'
    success_url = reverse_lazy('WOMbasic:home')


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Recipe.objects.filter(recipe_name__contains=searched)
        return render(request, 'WOMbasic/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'WOMbasic/search_results.html', {})


