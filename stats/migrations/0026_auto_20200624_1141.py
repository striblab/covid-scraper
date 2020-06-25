# Generated by Django 3.0.7 on 2020-06-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0025_statewidetestsdate_new_tests_rolling'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatewideDeathsDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_deaths', models.IntegerField(default=0)),
                ('new_tests_rolling', models.FloatField(default=0)),
                ('total_deaths', models.IntegerField(default=0)),
                ('update_date', models.DateField(null=True)),
                ('scrape_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='statewidetotaldate',
            old_name='new_deaths',
            new_name='deaths_daily_change',
        ),
    ]
