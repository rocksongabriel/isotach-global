# Generated by Django 3.2.10 on 2022-01-03 16:56

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='Date Uploaded')),
                ('title', models.CharField(default='', help_text='Example: 3 bedroom apartment at Kumasi, Ghana.', max_length=250, verbose_name='Title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('for_sale', models.BooleanField(default=False, help_text='Is this apartment for sale?', verbose_name='For Sale')),
                ('for_rent', models.BooleanField(default=True, help_text='Is this apartment for rent?', verbose_name='For Rent')),
                ('available', models.BooleanField(default=True, help_text='Check this box if the apartment has NOT been rented out.', verbose_name='Available')),
                ('location', models.CharField(help_text='Where is this apartment located?', max_length=50, verbose_name='Location')),
                ('bedrooms', models.PositiveSmallIntegerField(default=1, help_text='What is the total number of bedrooms in this apartment?', verbose_name='Number of Bedrooms')),
                ('baths', models.PositiveSmallIntegerField(default=1, help_text='How many baths are in this apartment?', verbose_name='Number of Baths')),
                ('hall', models.BooleanField(default=False, help_text='Does this apartment have a hall? Tick if yes.', verbose_name='Hall')),
                ('self_contained', models.BooleanField(default=True, help_text='Is this apartment self contained? Tick if yes.', verbose_name='Self Contained')),
                ('advance_years', models.PositiveSmallIntegerField(default=1, help_text='If this place is being rented out, how many years of advance payment is required?', verbose_name='Years of Advance Payment')),
                ('monthly_rent_payment', models.PositiveSmallIntegerField(help_text='How much is a tenant going to pay for the place every month?', verbose_name='Monthly Rent Payment')),
                ('description', models.TextField(help_text='Enter any extra details the potential occupant needs to know', verbose_name='Extra Description')),
                ('total_rent_payment', models.PositiveIntegerField(help_text='Amount tenant will pay over years of residency, monthly_payment * advance_years', verbose_name='Total Rent Payment')),
                ('agent_commission', models.PositiveSmallIntegerField(default=5, help_text='What is the commission the agent will take, in percentage.', verbose_name="Agent's Commission ( percentage )")),
                ('agent_fee', models.PositiveSmallIntegerField(help_text='Amount to pay to the agent.', verbose_name="Agent's Fee ( amount )")),
                ('inspection_fee', models.PositiveSmallIntegerField(default=50, help_text='How much is this agent charging potential clients to go show them the place?', verbose_name='Inspectoion Fee')),
                ('verified', models.BooleanField(default=False, help_text='Has this apartment been verified? Tick if Yes', verbose_name='Verified')),
            ],
            options={
                'verbose_name': 'Apartment',
                'verbose_name_plural': 'Apartments',
                'ordering': ('upload_time',),
            },
        ),
    ]
