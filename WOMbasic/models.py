from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    recipe_name = models.CharField(max_length=200, default="")
    publisher = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=datetime.now)
    recipe_description = models.TextField(default="")
    recipe_image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default_image.png")

    objects = models.Manager()

    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('WOMbasic:recipe-details', args=(str(self.pk)))
