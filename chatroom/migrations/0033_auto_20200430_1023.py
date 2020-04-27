# Generated by Django 3.0.5 on 2020-04-30 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('chatroom', '0032_auto_20200430_1023'),
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
