# Generated by Django 3.0.5 on 2020-05-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0006_auto_20200516_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='file', upload_to='post_images'),
        ),
    ]
