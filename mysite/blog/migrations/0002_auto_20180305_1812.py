# Generated by Django 2.0.2 on 2018-03-05 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_dated',
            new_name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 5, 10, 12, 8, 615169, tzinfo=utc)),
        ),
    ]
