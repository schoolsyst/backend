# Generated by Django 2.2.6 on 2019-10-11 06:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultsetting',
            name='positive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='defaultsetting',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID'),
        ),
    ]