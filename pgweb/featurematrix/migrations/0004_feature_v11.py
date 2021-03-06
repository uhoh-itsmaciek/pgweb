# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featurematrix', '0003_feature_v10'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='v11',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Obsolete'), (3, '?')], default=0, verbose_name='11'),
        ),
        migrations.RunSQL("UPDATE featurematrix_feature SET v11=v10 WHERE NOT v11=v10"),
    ]
