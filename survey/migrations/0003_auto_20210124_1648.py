# Generated by Django 3.1.5 on 2021-01-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_remove_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='Default question', max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='Default question', max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('question', 'choice_text')},
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('question_text',)},
        ),
    ]