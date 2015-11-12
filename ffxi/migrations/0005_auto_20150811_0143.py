# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ffxi', '0004_auto_20150811_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=b'2015-08-11')),
                ('exp', models.PositiveIntegerField(default=0)),
                ('chain', models.DecimalField(max_digits=4, decimal_places=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='dailytasks',
            old_name='exp_chain',
            new_name='chain',
        ),
    ]
