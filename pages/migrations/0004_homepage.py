# Generated by Django 3.2.10 on 2022-01-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20220106_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(help_text='Choose an image that will be featured on the banner of the homepage', upload_to='featured_images/homepage/', verbose_name='Banner Image')),
                ('banner_heading_text', models.CharField(default='Discover Your Perfect Home', help_text='Enter the text that will be displayed boldly on the banner on the homepage', max_length=100, verbose_name='Banner Heading Text')),
                ('banner_sub_heading_text', models.CharField(default='Search nearby for apartments, and homes for rent.', help_text='Enter the text that will be displayed below the bold text on the banner', max_length=130, verbose_name='Banner Sub Heading Text')),
            ],
        ),
    ]
