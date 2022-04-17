from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this


# Create your models here.
class Recipe(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    recipe_name = models.CharField(max_length=200, default="")
    publisher = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=datetime.now)
    recipe_description = models.TextField(default="")
    recipe_image = models.ImageField(null=True, blank=True, upload_to="images/", default="{% static 'WOMbasic/default_image.png' %}")

    objects = models.Manager()

    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('WOMbasic:recipe-details', args=(str(self.pk)))


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)