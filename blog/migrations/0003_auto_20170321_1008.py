# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_documenttype_field_filling_userdata_value_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileForm',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': 'Описание поля', 'verbose_name_plural': ' Описания полей'},
        ),
    ]
