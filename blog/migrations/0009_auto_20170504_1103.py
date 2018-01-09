# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170503_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='filling',
            name='chief_fullposition',
            field=models.CharField(max_length=30, default='some string'),
        ),
        migrations.AddField(
            model_name='filling',
            name='chief_name',
            field=models.CharField(max_length=30, default='some string'),
        ),
        migrations.AddField(
            model_name='filling',
            name='chief_secondname',
            field=models.CharField(max_length=30, default='some string'),
        ),
        migrations.AddField(
            model_name='filling',
            name='chief_surname',
            field=models.CharField(max_length=30, default='some string'),
        ),
    ]
