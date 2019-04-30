# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 11:42

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.db.models.fields import SlugField
import versionfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flow', '0001_squashed_0030_change_slug_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', SlugField(editable=True, max_length=100)),
                ('version', versionfield.VersionField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('settings', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('descriptor', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('collections', models.ManyToManyField(to='flow.Collection')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('data', models.ManyToManyField(to='flow.Data')),
                ('descriptor_schema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='flow.DescriptorSchema')),
                ('public_processes', models.ManyToManyField(to='flow.Process')),
            ],
            options={
                'default_permissions': (),
                'abstract': False,
                'permissions': (('view_sample', 'Can view sample'), ('edit_sample', 'Can edit sample'), ('share_sample', 'Can share sample'), ('download_sample', 'Can download files from sample'), ('add_sample', 'Can add data objects to sample')),
            },
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=set([('slug', 'version')]),
        ),
    ]
