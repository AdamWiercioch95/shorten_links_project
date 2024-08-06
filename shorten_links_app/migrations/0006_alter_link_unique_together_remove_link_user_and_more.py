# Generated by Django 5.0.7 on 2024-08-06 13:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten_links_app', '0005_alter_link_original_url_alter_link_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='link',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='link',
            name='user',
        ),
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ManyToManyField(related_name='links', to=settings.AUTH_USER_MODEL),
        ),
    ]
