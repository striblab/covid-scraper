# Generated by Django 3.0.7 on 2020-07-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0029_auto_20200703_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='statewidetotaldate',
            name='hospitalized_total_daily_change',
            field=models.IntegerField(default=0, null=True),
        ),
    ]