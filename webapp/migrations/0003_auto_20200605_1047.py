# Generated by Django 3.0.6 on 2020-06-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200605_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiods',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activityperiods',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
