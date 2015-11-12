# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxi', '0011_auto_20150826_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytally',
            name='date',
            field=models.DateField(default=b'2015-09-05'),
        ),
        migrations.AlterField(
            model_name='experiencehistory',
            name='date',
            field=models.DateField(default=b'2015-09-05'),
        ),
    ]
