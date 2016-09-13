# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 09:56
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=20)),
                ('feature_id', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[(b'gene', b'Gene'), (b'transcript', b'Transcript'), (b'exon', b'Exon'), (b'probe', b'Probe')], max_length=20)),
                ('sub_type', models.CharField(choices=[(b'protein-coding', b'Protein-coding'), (b'pseudo', b'Pseudo'), (b'rRNA', b'rRNA'), (b'ncRNA', b'ncRNA'), (b'snRNA', b'snRNA'), (b'snoRNA', b'snoRNA'), (b'tRNA', b'tRNA'), (b'other', b'Other'), (b'unknown', b'Unknown')], max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('full_name', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('aliases', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=[], size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[(b'crossdb', b'Crossdb'), (b'ortholog', b'Ortholog')], max_length=20)),
                ('source_db', models.CharField(max_length=20)),
                ('source_id', models.CharField(max_length=50)),
                ('target_db', models.CharField(max_length=20)),
                ('target_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('source', 'feature_id')]),
        ),
    ]
