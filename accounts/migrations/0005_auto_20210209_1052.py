# Generated by Django 3.1.3 on 2021-02-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210207_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/profile-images/'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]