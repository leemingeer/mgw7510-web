# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgw7510', '0006_auto_20161219_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webuser',
            name='email',
        ),
    ]
