# Generated by Django 5.0.7 on 2024-08-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten_links_app', '0003_remove_link_shortened_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='original_url',
            field=models.URLField(unique=True),
        ),
    ]