# Generated by Django 4.0.2 on 2022-04-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOMbasic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]