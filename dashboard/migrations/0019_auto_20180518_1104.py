# Generated by Django 2.0.5 on 2018-05-18 10:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20180518_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 18, 10, 4, 12, 696965, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Plan'),
        ),
        migrations.AlterField(
            model_name='match',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]