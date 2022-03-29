from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User
from . models import Recipe
# Create your tests here.
class RecipeTest(TestCase):

    def setUp(self):
        testUser = User.objects.createUser()
        self.recipe = Recipe.objects.create(publisher = User, recipe_name = 'test', date_published = datetime.now, recipe_description ='testdesc')

    def test_recipe_model(self):
        t = self.recipe
        self.assertTrue(isinstance(t, Recipe))
