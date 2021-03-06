# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-17 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170517_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='w_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='w_lastname',
            new_name='second_name',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='w_surname',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='chief_fullposition',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='chief_name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='chief_secondname',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='chief_surname',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='author_id',
        ),
        migrations.AddField(
            model_name='organization',
            name='chief',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chief', to='blog.Worker', verbose_name='Руководитель'),
        ),
        migrations.AddField(
            model_name='organization',
            name='fact_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Фактический адрес'),
        ),
        migrations.AddField(
            model_name='organization',
            name='post_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Почтовый адрес'),
        ),
        migrations.AddField(
            model_name='organization',
            name='reg_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Юридический адрес'),
        ),
        migrations.AddField(
            model_name='worker',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='blog.Organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование организации'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ogrn',
            field=models.CharField(max_length=13, verbose_name='ОГРН'),
        ),
    ]
