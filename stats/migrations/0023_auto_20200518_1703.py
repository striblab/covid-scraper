# Generated by Django 3.0.6 on 2020-05-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0022_auto_20200518_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statewidetotaldate',
            name='cases_removed',
        ),
        migrations.RemoveField(
            model_name='statewidetotaldate',
            name='new_cases',
        ),
        migrations.AddField(
            model_name='county',
            name='pop_2019',
            field=models.IntegerField(null=True),
        ),
    ]