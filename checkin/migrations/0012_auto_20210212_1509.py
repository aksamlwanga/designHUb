# Generated by Django 3.1.6 on 2021-02-12 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0011_auto_20210212_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
