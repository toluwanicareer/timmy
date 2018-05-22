# Generated by Django 2.0.5 on 2018-05-18 14:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20180518_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='pay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Payment'),
        ),
        migrations.AlterField(
            model_name='match',
            name='bitcoin_value',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=70, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='expiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 18, 14, 55, 38, 60702, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='investment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investment', to='dashboard.Investment'),
        ),
        migrations.AlterField(
            model_name='match',
            name='payer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Plan'),
        ),
        migrations.AlterField(
            model_name='match',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='time_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='time_matched',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]