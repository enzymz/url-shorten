# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('user_ip', models.CharField(max_length=50)),
                ('user_national', models.CharField(max_length=50)),
                ('short_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorturl.UrlShort')),
            ],
        ),
    ]
