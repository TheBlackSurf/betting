# Generated by Django 4.0.5 on 2022-06-14 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0021_remove_kolejka_user_kolejka_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kolejka',
            name='user',
        ),
        migrations.AddField(
            model_name='kolejka',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
