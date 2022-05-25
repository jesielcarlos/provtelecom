# Generated by Django 3.2.13 on 2022-05-25 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20220523_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contas',
            name='service_plan',
        ),
        migrations.AddField(
            model_name='contas',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Closed')], default=0, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='contas',
            name='payment_receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finance.paymentreceipt', verbose_name='Payment Receipt'),
        ),
        migrations.DeleteModel(
            name='ServicePlan',
        ),
    ]
