# Generated by Django 4.0.1 on 2022-02-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0023_remove_file_models_fm_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar_profile',
            name='sp_userid',
        ),
    ]
