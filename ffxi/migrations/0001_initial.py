# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=b'2015-08-10')),
                ('steps', models.PositiveIntegerField(default=0)),
                ('pushups', models.PositiveSmallIntegerField(default=0)),
                ('situps', models.PositiveSmallIntegerField(default=0)),
                ('squats', models.PositiveSmallIntegerField(default=0)),
                ('jumpjacks', models.PositiveSmallIntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='dailytasks',
            unique_together=set([('user', 'date')]),
        ),
    ]
