# Generated by Django 4.2.3 on 2023-07-25 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='facebook_link',
            new_name='social_link',
        ),
    ]