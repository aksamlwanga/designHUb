# Generated by Django 3.1.6 on 2021-02-07 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0002_auto_20210207_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='company',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]