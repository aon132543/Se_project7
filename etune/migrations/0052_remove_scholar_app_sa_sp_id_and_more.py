# Generated by Django 4.0.1 on 2022-02-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0051_alter_avatar_profile_sp_path_to_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar_app',
            name='sa_sp_id',
        ),
        migrations.AlterField(
            model_name='scholar_app',
            name='sa_score_info',
            field=models.JSONField(blank=True),
        ),
    ]