# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ffxi', '0006_auto_20150811_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedCharacters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_id', models.PositiveIntegerField(unique=True)),
                ('name', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='date',
            field=models.DateField(default=b'2015-08-12'),
        ),
        migrations.AlterField(
            model_name='experiencehistory',
            name='date',
            field=models.DateField(default=b'2015-08-12'),
        ),
    ]
