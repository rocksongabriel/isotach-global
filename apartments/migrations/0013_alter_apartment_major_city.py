# Generated by Django 3.2.11 on 2022-01-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0012_auto_20220122_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='major_city',
            field=models.CharField(choices=[('AC', 'Accra'), ('KU', 'Kumasi'), ('KO', 'Koforidua'), ('SU', 'Sunyani'), ('TA', 'Tamale'), ('KA', 'Kasoa'), ('CC', 'Cape Coast'), ('TM', 'Tema')], default='KU', help_text='Please select the major city that your apartment is located in.', max_length=20, verbose_name='Major City'),
        ),
    ]
