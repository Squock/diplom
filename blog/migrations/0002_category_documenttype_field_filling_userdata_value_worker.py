# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('types', models.CharField(max_length=30)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'verbose_name_plural': 'Описания полей',
                'verbose_name': 'Описание поля',
            },
        ),
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('inn', models.IntegerField(max_length=13)),
                ('ogrn', models.IntegerField(max_length=13)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.TextField()),
                ('field', models.ForeignKey(to='blog.Field')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('w_name', models.CharField(max_length=30)),
                ('w_surname', models.CharField(max_length=30)),
                ('w_lastname', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
