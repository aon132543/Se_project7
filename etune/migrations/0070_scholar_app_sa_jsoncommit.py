# Generated by Django 4.0.2 on 2022-02-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etune', '0069_alter_scholar_news_sn_photo_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholar_app',
            name='sa_jsoncommit',
            field=models.JSONField(default='{}'),
        ),
    ]
