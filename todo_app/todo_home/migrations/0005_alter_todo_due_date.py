# Generated by Django 4.2 on 2023-04-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_home', '0004_alter_todo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(),
        ),
    ]