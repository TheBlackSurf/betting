# Generated by Django 4.0.5 on 2022-07-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_comment_author_alter_comment_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='comment',
        ),
    ]
