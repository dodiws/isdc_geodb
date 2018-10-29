# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='forecastedLastUpdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datadate', models.DateTimeField()),
                ('forecasttype', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'forecastedlastupdate',
                'managed': True,
            },
        ),
    ]
