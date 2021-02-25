# Generated by Django 3.1.3 on 2021-02-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0054_auto_20210209_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatewideRaceDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_date', models.DateField(db_index=True)),
                ('race_eth', models.CharField(max_length=100)),
                ('cases_total', models.IntegerField(default=None, null=True)),
                ('deaths_total', models.IntegerField(default=None, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
