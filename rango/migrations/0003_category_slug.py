# Generated by Django 4.1.7 on 2023-03-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_alter_category_options_category_likes_category_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]