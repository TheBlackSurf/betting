# Generated by Django 4.0.5 on 2022-07-03 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_kolejka_name_alter_post_kolejka'),
        ('info', '0017_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]