# Generated by Django 2.1.2 on 2019-06-05 11:44

import Venter.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0033_auto_20190605_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to=Venter.helpers.get_user_profile_picture_path),
        ),
    ]
