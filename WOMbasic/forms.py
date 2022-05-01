
from django import forms
from .models import Recipe, Comment
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('publisher', 'recipe_name', 'recipe_description', 'recipe_steps', 'ingredients', 'recipe_image')

        widgets = {
            'publisher': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'pub', 'type': 'hidden'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder':
                                                        "Enter any relevant details, background, or fun facts about"
                                                        " your recipe to be shown on the home page."
                                                        }),
            'recipe_steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder':
                                                  "Start each step with a number on a new line"
                                                  "\nExample:"
                                                  "\n1. *** Step 1 ***"
                                                  "\n2. *** Step 2 ***"
                                                  "\n3. ..."
                                                  "\n4. ..."
                                                  }),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder':
                                                 "List each ingredient with a dash on a new line"
                                                 "\nExample:"
                                                 "\n- 4 tbsp butter"
                                                 "\n- 2 whole chicken breasts"
                                                 "\n- ..."
                                                 "\n- ..."
                                                 }),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ForkForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('publisher', 'recipe_name', 'recipe_description', 'recipe_steps', 'ingredients', 'recipe_image', 'forked')

        widgets = {
            'publisher': forms.TextInput(
                attrs={'class': 'form-control', 'value': '', 'id': 'pub', 'type': 'hidden'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'rn'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control', 'value': '', 'rows': 2, 'id': 'rd'}),
            'recipe_steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control'}),
            'forked': forms.CheckboxInput(
                attrs={'class': 'form-control', 'checked': True, 'value': 'on', 'id': 'forking', 'type': 'hidden'}),
            'forked_from': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'forked_fromId': forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }