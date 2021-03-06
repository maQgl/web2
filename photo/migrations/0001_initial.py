# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.Client')),
                ('img_url', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_author', to='client.Client')),
            ],
            options={
                'abstract': False,
            },
            bases=('client.client',),
        ),
    ]
