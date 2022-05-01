
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this


# Create your models here.
class Recipe(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    recipe_name = models.CharField(max_length=200, default="", verbose_name='Name of Recipe')
    publisher = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=datetime.now)
    recipe_description = models.TextField(default="", verbose_name='Brief Description')
    recipe_steps = models.TextField(default="", verbose_name='Step-by-Step Instructions')
    ingredients = models.TextField(default="")
    recipe_image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default_image.png",
                                     verbose_name='Picture of Recipe')
    forked = models.BooleanField(default=False)
    forked_from = models.TextField(default="")
    forked_fromId = models.IntegerField(default=1)
    likes = models.ManyToManyField(User, related_name='recipe_post')



    objects = models.Manager()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('WOMbasic:recipe-details', args=(str(self.pk)))


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name ="comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' %(self.recipe.recipe_name, self.name)