# Generated by Django 4.1.1 on 2022-11-11 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 11, 14, 54, 11, 98608), null=True),
        ),
    ]
