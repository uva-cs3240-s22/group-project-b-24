from django.shortcuts import render

from django.http import HttpResponse
from . models import Recipe


def insert(request):
    try:
        sub_text = request.POST['recipe']
    except KeyError:
        sub_text = "oopsies"
        return render(request, 'WOMbasic/submit.html')
    else:
        r = Recipe()
        r.recipe_text = request.POST.get('recipe', "empty")
        r.save()
        return render(request, 'WOMbasic/submit.html')

def listView(request):
    latest_recipe_list = Recipe.objects.order_by()
    context = {'latest_recipe_list': latest_recipe_list,}
    return render(request, 'WOMbasic/recipe.html', context)

def welcomeView(request):
    return render(request, 'WOMbasic/welcome.html')