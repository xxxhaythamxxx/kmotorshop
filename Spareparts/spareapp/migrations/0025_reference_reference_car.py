# Generated by Django 3.2.3 on 2021-06-05 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0024_auto_20210604_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='reference_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spareapp.car'),
        ),
    ]
