# Generated by Django 4.0.5 on 2022-06-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_vote_post_post_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='vote',
        ),
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.ManyToManyField(blank=True, null=True, related_name='siema', to='core.vote'),
        ),
    ]
