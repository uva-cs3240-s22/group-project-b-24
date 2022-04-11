
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_description', 'recipe_image')

        widgets = {
            #   'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control'}),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

