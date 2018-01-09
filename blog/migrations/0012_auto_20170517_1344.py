# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_delete_documenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('inn', models.IntegerField(verbose_name='ИНН')),
                ('ogrn', models.IntegerField(verbose_name='ОГРН')),
                ('name', models.CharField(verbose_name='Наименование организации', max_length=30)),
                ('city', models.CharField(verbose_name='Город', max_length=30)),
                ('address', models.CharField(verbose_name='Адрес', max_length=30)),
                ('chief_name', models.CharField(verbose_name='Имя', default='some string', max_length=30)),
                ('chief_surname', models.CharField(verbose_name='Фамилия', default='some string', max_length=30)),
                ('chief_secondname', models.CharField(verbose_name='Отчество', default='some string', max_length=30)),
                ('chief_fullposition', models.CharField(verbose_name='Должность', default='some string', max_length=30)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='filling',
            name='author_id',
        ),
        migrations.AlterField(
            model_name='orgdata',
            name='doc',
            field=models.ForeignKey(to='blog.Organization'),
        ),
        migrations.DeleteModel(
            name='Filling',
        ),
    ]
