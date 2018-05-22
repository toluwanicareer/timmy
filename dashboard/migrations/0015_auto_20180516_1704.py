# Generated by Django 2.0.5 on 2018-05-16 16:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20180516_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Awaiting Payment', max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('completion_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='investment',
            name='status',
            field=models.CharField(default='Maturing', max_length=200),
        ),
        migrations.AlterField(
            model_name='match',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 16, 4, 11, 559165, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='investment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Investment'),
        ),
    ]