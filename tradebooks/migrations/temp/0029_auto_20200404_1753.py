# Generated by Django 2.2.3 on 2020-04-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0028_auto_20200404_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='bookID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default='qj4Mho', unique=True),
        ),
    ]
