# Generated by Django 3.1.3 on 2020-12-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0003_auto_20201210_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='uploaded'),
        ),
    ]
