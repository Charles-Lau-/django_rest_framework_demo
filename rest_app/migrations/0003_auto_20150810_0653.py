# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_blog_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(related_name='blogs', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
