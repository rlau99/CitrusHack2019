# Generated by Django 2.1.5 on 2019-02-27 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0012_auto_20190221_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
