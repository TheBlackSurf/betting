# Generated by Django 4.0.5 on 2022-06-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_regulation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_on',)},
        ),
        migrations.AddField(
            model_name='vote',
            name='color_vote',
            field=models.CharField(blank=True, choices=[('Zółty', 'Zółty'), ('Pomarańczowy', 'Pomarańczowy'), ('Czerwony', 'Czerwony'), ('Zielony', 'Zielony')], max_length=200, null=True),
        ),
    ]
