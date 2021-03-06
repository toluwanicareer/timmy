# Generated by Django 2.0.5 on 2018-05-12 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=250)),
                ('day_length', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='match',
            old_name='status',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='match',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='match',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='match',
            name='user_to',
        ),
        migrations.AddField(
            model_name='match',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Plan'),
        ),
    ]
