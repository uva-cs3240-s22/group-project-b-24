
from django import forms
from django.forms.models import inlineformset_factory
from .models import Recipe, Ingredients


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('publisher', 'recipe_name', 'recipe_description', 'recipe_image')

        widgets = {
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control'}),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

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