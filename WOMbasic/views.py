from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from . models import Recipe
from . forms import RecipeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from . forms import RecipeForm, ForkForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

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
        results = Recipe.objects.filter(Q(recipe_name__icontains=searched) | Q(publisher__username__icontains=searched))
        return render(request, 'WOMbasic/search_results.html', {'searched': searched, 'results': results})
    else:
        return render(request, 'WOMbasic/search_results.html', {})

def LikeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    recipe.likes.add(request.user)
    return HttpResponseRedirect(reverse('WOMbasic:recipe-details', args=[str(pk)]))
