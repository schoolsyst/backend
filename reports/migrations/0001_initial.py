# Generated by Django 2.2.8 on 2020-01-12 20:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('type', models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Fonctionnalité')], max_length=7)),
                ('by_email', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('fr', 'Français'), ('en', 'English')], max_length=2)),
                ('github_issue', models.PositiveIntegerField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now=True)),
                ('happened', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.TextField()),
                ('url', models.URLField()),
                ('browser', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('device', models.CharField(choices=[('PHONE', 'Smartphone'), ('TABLET', 'Tablette'), ('LAPTOP', 'Ordinateur portable'), ('DESKTOP', 'Ordinateur fixe'), ('SMARTWATCH', 'Montre connectée'), ('OTHER', 'Autre')], max_length=10)),
                ('screen_size', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('(\\d+)x(\\d+)')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
