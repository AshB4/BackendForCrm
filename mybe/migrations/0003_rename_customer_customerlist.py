# Generated by Django 3.2.12 on 2024-03-23 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybe', '0002_customer_customerorder_equipmentlisting_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='CustomerList',
        ),
    ]
