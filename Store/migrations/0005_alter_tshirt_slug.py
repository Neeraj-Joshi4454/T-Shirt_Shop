# Generated by Django 4.0 on 2021-12-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_tshirt_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
