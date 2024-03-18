# Generated by Django 5.0.3 on 2024-03-18 06:53

import linkshortener.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkshortener', '0004_mylink_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylink',
            name='hash',
            field=models.CharField(default=linkshortener.utils.generate_unique_hash, max_length=50, unique=True),
        ),
    ]