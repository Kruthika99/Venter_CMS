# Generated by Django 2.1.2 on 2019-07-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0043_auto_20190719_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_name',
            field=models.CharField(max_length=200),
        ),
    ]