# Generated by Django 3.2.10 on 2022-01-07 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_apartment_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'ordering': ('-upload_time',), 'verbose_name': 'Apartment', 'verbose_name_plural': 'Apartments'},
        ),
    ]
