# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailytasks',
            name='situps',
        ),
        migrations.AddField(
            model_name='dailytasks',
            name='climbers',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailytasks',
            name='cross_crunches',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailytasks',
            name='high_knees',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailytasks',
            name='knee_pull_ins',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailytasks',
            name='plank_jumps',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
