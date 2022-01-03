# Generated by Django 3.2.10 on 2022-01-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='agent_fee',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Amount to pay to the agent.', null=True, verbose_name="Agent's Fee ( amount )"),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(blank=True, help_text='Enter any extra details the potential occupant needs to know', null=True, verbose_name='Extra Description'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='inspection_fee',
            field=models.PositiveSmallIntegerField(default=50, help_text='How much is this agent charging potential clients to go show them the place?', verbose_name='Inspection Fee'),
        ),
    ]