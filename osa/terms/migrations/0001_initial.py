# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(choices=[('S', 'SPRING'), ('M', 'SUMMER'), ('F', 'FALL')], max_length=1)),
                ('year', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
