# Generated by Django 3.1.6 on 2021-02-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0008_auto_20210212_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
