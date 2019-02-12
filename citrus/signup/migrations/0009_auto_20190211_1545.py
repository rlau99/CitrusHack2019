# Generated by Django 2.1.5 on 2019-02-11 23:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_auto_20190211_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='learn_or_gain',
            field=models.TextField(default='', validators=[django.core.validators.MinLengthValidator(250), django.core.validators.MaxLengthValidator(1000)]),
        ),
    ]
