# Generated by Django 3.2.13 on 2022-05-25 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceplan',
            name='bandwidth',
        ),
        migrations.RemoveField(
            model_name='serviceplan',
            name='description',
        ),
        migrations.RemoveField(
            model_name='serviceplan',
            name='type_service',
        ),
        migrations.RemoveField(
            model_name='serviceplan',
            name='value',
        ),
        migrations.RemoveField(
            model_name='serviceplan',
            name='velocity',
        ),
    ]
