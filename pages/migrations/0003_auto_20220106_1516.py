# Generated by Django 3.2.10 on 2022-01-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_aboutsection_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsection',
            name='name',
            field=models.CharField(default='', max_length=10, verbose_name='Name of Section'),
        ),
        migrations.AddField(
            model_name='servicessection',
            name='name',
            field=models.CharField(default='', max_length=10, verbose_name='Name of Section'),
        ),
    ]
