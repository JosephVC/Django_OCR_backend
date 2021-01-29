# Generated by Django 3.1.5 on 2021-01-29 18:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('file', models.FileField(default='file', upload_to='post_files')),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=250, unique_for_date='uploaded')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
