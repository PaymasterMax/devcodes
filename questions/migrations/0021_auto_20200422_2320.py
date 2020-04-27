# Generated by Django 3.0.5 on 2020-04-22 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('questions', '0020_merge_20200422_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='auid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answerer', to='signup.Signup'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='question_to_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_to_answer', to='questions.Questions'),
        ),
        migrations.AlterField(
            model_name='questionlike',
            name='Qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_liked', to='questions.Questions'),
        ),
        migrations.AlterField(
            model_name='questionlike',
            name='luid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Qliker', to='signup.Signup'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='quid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_asker', to='signup.Signup'),
        ),
    ]
