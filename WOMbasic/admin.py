from django.contrib import admin
from .models import Recipe, Ingredients

class IngredientsInLineAdmin(admin.TabularInline):
    model = Ingredients

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientsInLineAdmin]

admin.site.register(Recipe, RecipeAdmin)