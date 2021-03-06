# Generated by Django 3.2.8 on 2021-12-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('order_id', models.CharField(max_length=1000)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=1000)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]
