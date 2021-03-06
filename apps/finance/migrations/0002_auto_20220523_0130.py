# Generated by Django 3.2.13 on 2022-05-23 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileUser', '0002_auto_20220523_0130'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceplan',
            name='name',
            field=models.CharField(default='name', max_length=150, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serviceplan',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='serviceplan',
            name='dt_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='serviceplan',
            name='type_service',
            field=models.IntegerField(choices=[(0, 'Internet'), (1, 'Voip')], verbose_name='Type Service'),
        ),
        migrations.CreateModel(
            name='PaymentReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('dt_payment', models.DateTimeField(verbose_name='Date Payment')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profileUser.profileuser', verbose_name='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('dt_payment', models.DateTimeField(blank=True, null=True, verbose_name='Date Payment')),
                ('dt_due', models.DateTimeField(verbose_name='Date Due')),
                ('payment', models.IntegerField(choices=[(0, 'Card'), (1, 'Bank Ticket'), (2, 'Pix'), (3, 'Bank Transfer')], verbose_name='Payment')),
                ('payment_receipt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.paymentreceipt', verbose_name='Payment Receipt')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profileUser.profileuser', verbose_name='profile')),
                ('service_plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.serviceplan', verbose_name='Service Plan')),
            ],
        ),
    ]
