# Generated by Django 3.2.13 on 2022-05-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callSystem', '0002_called_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='called',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='called',
            name='situation',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Closed'), (2, 'In Progress')], default=0, verbose_name='Situation'),
        ),
        migrations.AlterField(
            model_name='called',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
