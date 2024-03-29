# Generated by Django 5.0.1 on 2024-01-25 07:19

import linkshortener.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkshortener', '0002_rename_shorted_link_mylink_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylink',
            name='slug',
        ),
        migrations.AddField(
            model_name='mylink',
            name='hash',
            field=models.CharField(default=linkshortener.utils.generate_unique_hash, max_length=300, unique=True),
        ),
    ]
