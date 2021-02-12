# Generated by Django 3.1.6 on 2021-02-07 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0003_auto_20210207_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='id_no',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
