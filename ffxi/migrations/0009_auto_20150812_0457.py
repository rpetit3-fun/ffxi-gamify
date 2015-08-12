# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxi', '0008_auto_20150812_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkedaccount',
            name='acc_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='linkedaccount',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]
