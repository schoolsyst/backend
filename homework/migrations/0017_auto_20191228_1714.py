# Generated by Django 2.2.6 on 2019-12-28 17:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0016_auto_20191221_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='expected',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, "This can't be greater than 1")], verbose_name='Expected grade'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='goal',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, "This can't be greater than 1")], verbose_name='Grade goal'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='obtained',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, "This can't be greater than 1")], verbose_name='Obtained grade'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='progress',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, "This can't be greater than 1")]),
        ),
    ]