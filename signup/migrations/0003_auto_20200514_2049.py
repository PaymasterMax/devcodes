# Generated by Django 3.0.6 on 2020-05-14 20:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20200509_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='profilepic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
