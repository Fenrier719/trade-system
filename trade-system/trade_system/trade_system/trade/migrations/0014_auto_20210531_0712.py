# Generated by Django 3.1.11 on 2021-05-31 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_remove_watchlistitem_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='whatchlist_items',
            new_name='watchlist_items',
        ),
    ]
