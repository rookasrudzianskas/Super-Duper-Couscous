# Generated by Django 3.2 on 2021-04-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_questions_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
