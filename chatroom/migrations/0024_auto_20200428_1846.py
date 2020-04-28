# Generated by Django 3.0.5 on 2020-04-28 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('chatroom', '0023_auto_20200428_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='r1uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to='signup.Signup'),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='r2uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to='signup.Signup'),
        ),
    ]
