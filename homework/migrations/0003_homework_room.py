# Generated by Django 2.2.6 on 2019-10-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_auto_20191011_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='room',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
