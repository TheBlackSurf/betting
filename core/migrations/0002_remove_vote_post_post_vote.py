# Generated by Django 4.0.5 on 2022-06-08 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siema', to='core.vote'),
        ),
    ]
