# Generated by Django 4.0.5 on 2022-06-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_alter_profilepoint_kolejka1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepoint',
            name='dodatkowepunkty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]