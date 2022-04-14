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
<<<<<<< HEAD
    likes = models.ManyToManyField(User, related_name='recipe_post')
=======
    forked = models.BooleanField(default=False)
    forked_from = models.TextField(default="")
    forked_fromId = models.IntegerField(default=1)
>>>>>>> searchfunction

    objects = models.Manager()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('WOMbasic:recipe-details', args=(str(self.pk)))
