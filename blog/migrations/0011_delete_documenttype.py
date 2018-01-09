# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170517_1328'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DocumentType',
        ),
    ]
