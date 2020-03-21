# Generated by Django 3.0.3 on 2020-03-20 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20200224_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneToOneProfile',
            fields=[
                ('fk_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('display_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('dob', models.DateField()),
                ('image_url', models.URLField(max_length=300)),
                ('Friends', models.ManyToManyField(blank=True, related_name='Friends', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]