# Generated by Django 5.0.7 on 2024-08-06 12:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten_links_app', '0004_alter_link_original_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='original_url',
            field=models.URLField(),
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together={('original_url', 'user')},
        ),
    ]
