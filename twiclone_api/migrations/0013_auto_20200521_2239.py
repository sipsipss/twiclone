# Generated by Django 3.0.6 on 2020-05-21 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twiclone_api', '0012_userprofile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.ManyToManyField(related_name='follows', to='twiclone_api.UserFollowers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
