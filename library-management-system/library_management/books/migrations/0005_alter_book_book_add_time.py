# Generated by Django 5.0.4 on 2024-04-24 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_book_add_date_alter_book_book_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_time',
            field=models.TimeField(default=datetime.datetime(2024, 4, 24, 9, 14, 29, 978750, tzinfo=datetime.timezone.utc)),
        ),
    ]
