# Generated by Django 2.1.2 on 2019-06-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Venter', '0034_auto_20190605_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Domain',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
                ('proposal_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Venter.Domain')),
            ],
            options={
                'verbose_name_plural': 'Keyword',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('proposal_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='proposal_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Venter.Proposal'),
        ),
        migrations.AddField(
            model_name='file',
            name='proposal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposal', to='Venter.Proposal'),
        ),
    ]
