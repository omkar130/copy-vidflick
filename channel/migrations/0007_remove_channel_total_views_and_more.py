# Generated by Django 5.1.6 on 2025-02-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channel", "0006_channel_bussiness_email_channel_bussiness_location_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="channel", name="total_views",),
        migrations.AlterField(
            model_name="channel",
            name="bussiness_email",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="channel",
            name="bussiness_location",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
