# Generated by Django 5.2.4 on 2025-07-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0007_alter_book_online_options_alter_book_online_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_service',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
