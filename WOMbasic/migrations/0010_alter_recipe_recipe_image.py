# Generated by Django 4.0.2 on 2022-04-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0009_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, default='images/Quiz2Problem2.jpeg', null=True, upload_to='images/'),
        ),
    ]