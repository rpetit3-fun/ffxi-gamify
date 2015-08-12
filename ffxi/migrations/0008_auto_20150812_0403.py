# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ffxi', '0007_auto_20150812_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc_id', models.PositiveIntegerField(unique=True)),
                ('name', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='linkedcharacters',
            name='user',
        ),
        migrations.DeleteModel(
            name='LinkedCharacters',
        ),
    ]
