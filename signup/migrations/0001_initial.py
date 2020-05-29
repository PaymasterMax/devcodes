# Generated by Django 3.0.6 on 2020-05-24 23:30

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('pnumber', models.IntegerField()),
                ('location', models.CharField(default='Nairobi/Kenya', max_length=30)),
                ('hobby', models.CharField(max_length=30)),
                ('profilepic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('password', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]