# Generated by Django 3.0.5 on 2020-04-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twiclone_api', '0006_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(max_length=280)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture'),
        ),
    ]