
from django import forms
from .models import Recipe
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('publisher', 'recipe_name', 'recipe_description', 'recipe_image')

        widgets = {
            'publisher': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'pub', 'type': 'hidden'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control'}),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ForkForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('publisher', 'recipe_name', 'recipe_description', 'recipe_image', 'forked')

        widgets = {
            'publisher': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'pub', 'type': 'hidden'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'rn'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control', 'value': '', 'id': 'rd'}),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control'}),
            'forked': forms.CheckboxInput(
                attrs={'class': 'form-control', 'checked': True, 'value': 'on', 'id': 'forking', 'type': 'hidden'}),
            'forked_from': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'forked_fromId': forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        }
