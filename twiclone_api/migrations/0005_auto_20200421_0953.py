# Generated by Django 3.0.5 on 2020-04-21 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twiclone_api', '0004_remove_user_username_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='website',
        ),
    ]