from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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


#class ForkRecipe(CreateView):
  # model = Recipe
   # form_class = ForkForm
   # template_name = 'WOMbasic/forksubmit.html'
   # success_url = reverse_lazy('WOMbasic:home')


def fork_recipe(request, pk1):
    frec = Recipe.objects.get(pk=pk1)
    frec_val = pk1
    frec.pk = None

    form = ForkForm(request.POST or None, instance=frec)

    if form.is_valid():
        form.instance.forked_fromId = pk1
        form.instance.forked_from = Recipe.objects.get(pk=frec_val).recipe_name
        form.save()
        return redirect('WOMbasic:home')

    return render(request, "WOMbasic/forksubmit.html", {'form': form})


def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Recipe.objects.filter(recipe_name__contains=searched)
        return render(request, 'WOMbasic/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'WOMbasic/search_results.html', {})

