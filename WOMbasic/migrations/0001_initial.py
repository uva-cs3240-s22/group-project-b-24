# Generated by Django 4.1.dev20220210102451 on 2022-03-13 20:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(default='', max_length=200)),
                ('date_published', models.DateTimeField(default=datetime.datetime.now)),
                ('recipe_description', models.TextField(default='')),
                ('recipe_image', models.ImageField(blank=True, default='/media/images/default_image.png', upload_to='media/images/')),
                ('publisher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
