# Generated by Django 3.2.13 on 2022-06-25 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileUser', '0007_alter_profileuser_service_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='theme_dark',
        ),
    ]
