# Generated by Django 4.0 on 2021-12-22 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Store', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('PLACED', 'Placed'), ('CANCELED', 'Canceled'), ('COMPLETED', 'Completed')], max_length=15)),
                ('payment_method', models.CharField(choices=[('COD', 'Cod'), ('ONLINE', 'Online')], max_length=15)),
                ('shiping_address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
                ('total', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_status', models.CharField(default='FAILED', max_length=15)),
                ('payment_id', models.CharField(max_length=60)),
                ('payment_request_id', models.CharField(max_length=60)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.order')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.sizevarient')),
                ('tshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.tshirt')),
            ],
        ),
    ]
