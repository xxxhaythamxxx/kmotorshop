# Generated by Django 3.2.3 on 2021-06-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0016_alter_car_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Category'),
        ),
    ]
