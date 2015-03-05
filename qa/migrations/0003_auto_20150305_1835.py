# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20150305_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='choice_text',
            new_name='answer_text',
        ),
    ]
