# Generated by Django 3.2.13 on 2022-05-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileUser', '0002_auto_20220523_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='theme_dark',
            field=models.BooleanField(default=True, verbose_name='Theme Dark'),
        ),
    ]
