# Generated by Django 2.2.3 on 2020-04-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0028_remove_listing_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='book',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
