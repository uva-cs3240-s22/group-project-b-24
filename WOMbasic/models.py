from django.db import models
from datetime import datetime
# Create your models here.
class Recipe(models.Model):
    publisher = models.EmailField(default="")
    recipe_name = models.CharField(max_length=200, default="")
    date_published = models.DateTimeField(default=datetime.now)
    recipe_description = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.recipe_name