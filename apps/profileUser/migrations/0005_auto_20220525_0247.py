# Generated by Django 3.2.13 on 2022-05-25 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileUser', '0004_auto_20220525_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='district',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='dt_created',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='number',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='service_plan',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='theme_dark',
        ),
    ]