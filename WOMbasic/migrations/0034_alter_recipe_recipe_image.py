# Generated by Django 4.0.2 on 2022-05-02 22:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0033_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left'], default='images/default_image.png', force_format='JPEG', keep_meta=True, null=True, quality=100, size=[600, 600], upload_to='images/', verbose_name='Picture of Recipe'),
        ),
    ]
