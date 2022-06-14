# Generated by Django 4.0.5 on 2022-06-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_settings_footercode_settings_headercode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footercode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HeaderCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headercore', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sitelanguage', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
