# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxi', '0005_auto_20150811_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencestats',
            name='chain',
            field=models.DecimalField(default=1.0, max_digits=4, decimal_places=2),
        ),
    ]
