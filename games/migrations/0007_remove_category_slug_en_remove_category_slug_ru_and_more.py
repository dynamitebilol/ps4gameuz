# Generated by Django 4.0.3 on 2022-07-23 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_category_slug_en_category_slug_ru_category_slug_uz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_uz',
        ),
        migrations.RemoveField(
            model_name='game',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='game',
            name='category_ru',
        ),
        migrations.RemoveField(
            model_name='game',
            name='category_uz',
        ),
    ]