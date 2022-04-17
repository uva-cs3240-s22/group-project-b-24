from django.contrib import admin

# Register your models here.
from.models import Recipe, Profile
admin.site.register(Recipe)
admin.site.register(Profile)