# Generated by Django 2.1.5 on 2019-03-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0015_auto_20190303_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender_other',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='race',
            field=models.CharField(choices=[(None, ''), ('American Indian or Alaskan Native', 'American Indian or Alaskan Native'), ('Asian/Pacific Islander', 'Asian/Pacific Islander'), ('Black or African American', 'Black or African American'), ('Hispanic', 'Hispanic'), ('White/Caucasian', 'White/Caucasian'), ('Multiple ethnicity/Other (Please Specify)', 'Multiple ethnicity/Other (Please Specify)'), ('Prefer not to diclose', 'Prefer not to disclose')], default='', max_length=45),
        ),
    ]
