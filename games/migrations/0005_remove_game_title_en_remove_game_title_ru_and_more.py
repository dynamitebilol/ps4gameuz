# Generated by Django 4.0.3 on 2022-07-23 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='game',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='game',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='herosection',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='herosection',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='herosection',
            name='title_uz',
        ),
    ]