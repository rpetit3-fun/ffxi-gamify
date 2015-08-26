# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ffxi', '0010_auto_20150817_0340'),
    ]

    operations = [
        migrations.RenameModel('DailyTasks', 'DailyTally')
    ]
