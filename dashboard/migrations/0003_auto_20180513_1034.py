# Generated by Django 2.0.5 on 2018-05-13 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20180512_2122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Evidences',
            new_name='Evidence',
        ),
    ]