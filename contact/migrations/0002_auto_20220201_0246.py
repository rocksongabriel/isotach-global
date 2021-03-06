# Generated by Django 3.2.11 on 2022-02-01 02:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Contact Message', 'verbose_name_plural': 'Contact Messages'},
        ),
        migrations.AddField(
            model_name='contactform',
            name='date_and_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
