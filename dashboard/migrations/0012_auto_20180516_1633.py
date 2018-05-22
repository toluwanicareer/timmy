# Generated by Django 2.0.5 on 2018-05-16 15:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20180516_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='completed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 15, 33, 13, 446579, tzinfo=utc), null=True),
        ),
    ]