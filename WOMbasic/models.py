from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Recipe(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200, default="")
    date_published = models.DateTimeField(default=datetime.now)
    recipe_description = models.TextField(default="")
    recipe_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.recipe_name + ' | ' + str(self.publisher)

    def get_absolute_url(self):
        return reverse('WOMbasic:recipe-details', args=(str(self.pk)))