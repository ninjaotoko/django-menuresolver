# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0021_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='item',
            field=models.ForeignKey(related_name='item', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='menuresolver.Item', null=True),
            preserve_default=True,
        ),
    ]