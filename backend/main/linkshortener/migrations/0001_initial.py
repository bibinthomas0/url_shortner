# Generated by Django 5.0.1 on 2024-01-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_link', models.CharField(max_length=300)),
                ('shorted_link', models.CharField(max_length=300)),
            ],
        ),
    ]
