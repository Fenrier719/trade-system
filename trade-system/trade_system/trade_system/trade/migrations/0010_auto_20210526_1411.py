# Generated by Django 3.1.11 on 2021-05-26 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0009_auto_20210526_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade.item', unique=True),
        ),
    ]
