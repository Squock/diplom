# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170321_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filling',
            name='inn',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filling',
            name='ogrn',
            field=models.IntegerField(),
        ),
    ]
