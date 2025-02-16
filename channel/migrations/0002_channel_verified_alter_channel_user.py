# Generated by Django 5.1.6 on 2025-02-14 19:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="channel",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="channel_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
