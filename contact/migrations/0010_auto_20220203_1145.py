# Generated by Django 3.2.11 on 2022-02-03 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0014_auto_20220123_2039'),
        ('contact', '0009_auto_20220202_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='agent_name',
            field=models.CharField(default='', max_length=50, verbose_name='Agent Name'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='apartment',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inquiries', to='apartments.apartment'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='apartment_title',
            field=models.CharField(default='', max_length=200, verbose_name='Apartment Title'),
        ),
    ]
