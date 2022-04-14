from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django.http import HttpResponse
from . models import Recipe
from . forms import RecipeForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

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

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(*args, **kwargs)

        stuff=get_object_or_404(Recipe, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context


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
        results = Recipe.objects.filter(recipe_name__contains=searched)
        return render(request, 'WOMbasic/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'WOMbasic/search_results.html', {})

def LikeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    recipe.likes.add(request.user)
    return HttpResponseRedirect(reverse('WOMbasic:recipe-details', args=[str(pk)]))
