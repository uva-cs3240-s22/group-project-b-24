# Generated by Django 4.0.2 on 2022-04-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0011_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, default='images/default_image.png', null=True, upload_to='images/'),
        ),
    ]