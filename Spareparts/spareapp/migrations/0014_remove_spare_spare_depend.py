# Generated by Django 3.2.3 on 2021-06-01 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0013_auto_20210531_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spare',
            name='spare_depend',
        ),
    ]
