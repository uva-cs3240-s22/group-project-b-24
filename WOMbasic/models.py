from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_text = models.CharField(max_length=200)
    def __str__(self):
        return self.recipe_text