# Generated by Django 3.2.10 on 2022-01-04 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20220104_0943'),
        ('apartments', '0003_apartmentimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='agent',
            field=models.ForeignKey(help_text='Which agent is in charge of this apartment?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='agents.agent', verbose_name='Agent'),
        ),
    ]
