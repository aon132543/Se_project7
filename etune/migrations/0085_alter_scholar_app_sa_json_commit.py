# Generated by Django 4.0.2 on 2022-02-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0084_alter_scholar_app_sa_json_commit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar_app',
            name='sa_json_commit',
            field=models.JSONField(default={}, null=True),
        ),
    ]
