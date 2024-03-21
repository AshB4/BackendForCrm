# Generated by Django 5.0.3 on 2024-03-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('listing_id', models.IntegerField()),
                ('customer', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentListing',
            fields=[
                ('listing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_id', models.IntegerField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesRepresentative',
            fields=[
                ('rep_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('payment_method', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
    ]