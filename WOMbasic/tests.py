from django.test import TestCase
from . models import Recipe
# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(recipe_text='test')

    def test_recipe_model(self):
        t = self.recipe
        self.assertTrue(isinstance(t, Recipe))
        self.assertEqual(str(t), 'test')
