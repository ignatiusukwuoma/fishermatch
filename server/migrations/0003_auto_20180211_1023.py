# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-11 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_remove_googleuser_slack_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stock', models.CharField(max_length=300)),
                ('vessels', models.CharField(max_length=300)),
                ('geography', models.CharField(max_length=300)),
                ('research_gaps', models.TextField()),
                ('details', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Fisher')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Fisher')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bio', models.TextField()),
                ('education', models.TextField()),
                ('experience', models.IntegerField()),
                ('research_experience', models.TextField()),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='match',
            name='researcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Researcher'),
        ),
        migrations.AddField(
            model_name='interest',
            name='researcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Researcher'),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='fisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Fisher'),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='researcher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Researcher'),
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('researcher', 'fisher')]),
        ),
        migrations.AlterUniqueTogether(
            name='interest',
            unique_together=set([('researcher', 'fisher')]),
        ),
    ]
