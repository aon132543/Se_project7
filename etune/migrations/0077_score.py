# Generated by Django 4.0.2 on 2022-02-26 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('etune', '0076_remove_scholar_app_sa_jsoncommit'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.JSONField()),
                ('ls_Scholar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etune.scholar_info')),
                ('ls_commit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
                ('ls_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
