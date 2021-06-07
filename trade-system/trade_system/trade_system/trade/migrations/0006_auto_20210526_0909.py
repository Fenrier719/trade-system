# Generated by Django 3.1.11 on 2021-05-26 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20210526_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='item',
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.currency'),
        ),
        migrations.RemoveField(
            model_name='offer',
            name='item',
        ),
        migrations.AddField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trade.item'),
        ),
        migrations.RemoveField(
            model_name='trade',
            name='item',
        ),
        migrations.AddField(
            model_name='trade',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trade.item'),
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trade.item'),
        ),
    ]
