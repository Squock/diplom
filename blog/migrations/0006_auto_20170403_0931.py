# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userdoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdoc',
            name='userFile',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
