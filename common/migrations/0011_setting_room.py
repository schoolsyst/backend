# Generated by Django 2.2.4 on 2019-08-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20190806_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='room',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
