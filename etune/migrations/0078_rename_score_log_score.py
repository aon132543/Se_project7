# Generated by Django 4.0.2 on 2022-02-26 04:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('etune', '0077_score'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='score',
            new_name='Log_score',
        ),
    ]
