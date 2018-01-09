# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170504_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttype',
            name='name',
            field=models.CharField(verbose_name='Наименование', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='chief_fullposition',
            field=models.CharField(default='some string', verbose_name='Должность', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='chief_name',
            field=models.CharField(default='some string', verbose_name='Имя', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='chief_secondname',
            field=models.CharField(default='some string', verbose_name='Отчество', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='chief_surname',
            field=models.CharField(default='some string', verbose_name='Фамилия', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='city',
            field=models.CharField(verbose_name='Город', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='inn',
            field=models.IntegerField(verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='name',
            field=models.CharField(verbose_name='Наименование организации', max_length=30),
        ),
        migrations.AlterField(
            model_name='filling',
            name='ogrn',
            field=models.IntegerField(verbose_name='ОГРН'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(verbose_name='Элекронная почта', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(verbose_name='Имя', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(verbose_name='Фамилия', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='number',
            field=models.CharField(verbose_name='Номер телефона', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='second_name',
            field=models.CharField(verbose_name='Отчество', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.CharField(verbose_name='Должность', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='w_lastname',
            field=models.CharField(verbose_name='Отчество', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='w_name',
            field=models.CharField(verbose_name='Имя', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='w_surname',
            field=models.CharField(verbose_name='Фамилия', max_length=30),
        ),
    ]
