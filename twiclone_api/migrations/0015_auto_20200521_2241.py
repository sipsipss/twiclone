# Generated by Django 3.0.6 on 2020-05-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twiclone_api', '0014_auto_20200521_2239'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFollowers',
            new_name='UserFollower',
        ),
    ]