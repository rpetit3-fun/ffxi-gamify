# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxi', '0003_experiencestats'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytasks',
            name='exp_chain',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='date',
            field=models.DateField(default=b'2015-08-11'),
        ),
        migrations.AlterField(
            model_name='experiencestats',
            name='chain',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
