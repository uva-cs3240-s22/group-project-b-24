# Generated by Django 4.0.2 on 2022-05-02 21:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0027_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/default_image.png', force_format='JPEG', keep_meta=True, null=True, quality=75, size=[100, 100], upload_to='images/', verbose_name='Picture of Recipe'),
        ),
    ]
