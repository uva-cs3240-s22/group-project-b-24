from django.shortcuts import render

from django.http import HttpResponse
from.models import Recipe


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def listView(request):
    latest_recipe_list = Recipe.objects.order_by()
    context = {'latest_recipe_list': latest_recipe_list,}
    return render(request, 'WOMbasic/recipe.html', context)