# Generated by Django 2.1.5 on 2019-03-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0014_merge_20190303_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender_other',
            field=models.CharField(blank=True, default='', max_length=45),
        ),
    ]
