# Generated by Django 4.0.5 on 2022-06-08 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_post_vote_vote_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
    ]
