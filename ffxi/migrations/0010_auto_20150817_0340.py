# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxi', '0009_auto_20150812_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnhancedSignetLevels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exp', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='date',
            field=models.DateField(default=b'2015-08-17'),
        ),
        migrations.AlterField(
            model_name='experiencehistory',
            name='date',
            field=models.DateField(default=b'2015-08-17'),
        ),
    ]
