# Generated by Django 4.2 on 2023-04-11 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='user',
        ),
    ]
