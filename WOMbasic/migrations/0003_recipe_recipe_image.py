# Generated by Django 4.1.dev20220210102451 on 2022-03-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0002_remove_recipe_recipe_text_recipe_date_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]