# Generated by Django 4.1.6 on 2023-02-28 05:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("propertyManager", "0012_propertydetail_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="propertydetail",
            name="is_active",
        ),
        migrations.AddField(
            model_name="propertydetail",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="propertydetail",
            name="rent_token",
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]
