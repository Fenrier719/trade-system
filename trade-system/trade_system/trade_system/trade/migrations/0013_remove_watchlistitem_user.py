# Generated by Django 3.1.11 on 2021-05-31 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0012_inventoryitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlistitem',
            name='user',
        ),
    ]
