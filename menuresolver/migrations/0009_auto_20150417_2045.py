# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0008_auto_20150417_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
