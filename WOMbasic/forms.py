
from django import forms
<<<<<<< HEAD
from django.forms.models import inlineformset_factory
from .models import Recipe, Ingredients
=======
from .models import Recipe
from django.contrib.auth.models import User
>>>>>>> 4ff4e201159140308d606e7edbe4a52691a3b3ac


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

<<<<<<< HEAD
class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = (
            'name',
            'serving_amount'
        )
IngredientsFormSet = inlineformset_factory(
    Recipe,
    Ingredients,
    IngredientsForm,
    min_num=2,  # minimum number of forms that must be filled in
    extra=1,  # number of empty forms to display
    can_delete=False  # show a checkbox in each form to delete the row
)
=======

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
>>>>>>> 4ff4e201159140308d606e7edbe4a52691a3b3ac
