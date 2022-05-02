# Generated by Django 4.0.2 on 2022-05-02 21:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0028_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='images/default_image.png', force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='images/', verbose_name='Picture of Recipe'),
        ),
    ]
