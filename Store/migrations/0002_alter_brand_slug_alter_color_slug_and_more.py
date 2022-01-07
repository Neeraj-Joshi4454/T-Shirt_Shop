# Generated by Django 4.0 on 2021-12-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='idealfor',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='necktype',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='occasion',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sleeve',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]