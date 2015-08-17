# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('title_id', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
            ],
        ),
    ]
