# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=100, verbose_name='code')),
                ('speed', models.BooleanField(default=False, verbose_name='track speed')),
                ('site', models.OneToOneField(verbose_name='site', to='sites.Site')),
            ],
            options={
                'ordering': ('site', 'code'),
                'verbose_name': 'analytics code',
                'verbose_name_plural': 'analytics codes',
            },
        ),
        migrations.CreateModel(
            name='SiteVerificationCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=100, verbose_name='code')),
                ('site', models.OneToOneField(verbose_name='site', to='sites.Site')),
            ],
            options={
                'ordering': ('site', 'code'),
                'verbose_name': 'site verification code',
                'verbose_name_plural': 'site verification codes',
            },
        ),
    ]
