# Generated by Django 5.1.7 on 2025-03-31 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_remove_journalentry_date_posted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentry',
            name='created_at',
        ),
        migrations.AddField(
            model_name='journalentry',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 3, 31, 17, 35, 55, 154683)),
            preserve_default=False,
        ),
    ]
