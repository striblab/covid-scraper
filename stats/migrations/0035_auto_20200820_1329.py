# Generated by Django 3.0.9 on 2020-08-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0034_auto_20200820_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='statewideagedate',
            name='age_max',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statewideagedate',
            name='age_min',
            field=models.IntegerField(null=True),
        ),
    ]
