# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20161118_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.User')),
            ],
        ),
    ]
