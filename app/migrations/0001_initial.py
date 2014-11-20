# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('pernom', models.CharField(max_length=30)),
                ('telephone_fix', models.CharField(max_length=16)),
                ('telephone_protable', models.CharField(max_length=16)),
                ('adress', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=30)),
                ('ville', models.CharField(max_length=50)),
                ('code_postal', models.CharField(max_length=10)),
                ('civilite', models.IntegerField()),
                ('date_naissance', models.DateField()),
                ('date_rdv', models.DateTimeField()),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('pernom', models.CharField(max_length=30)),
                ('telephone_protable', models.CharField(max_length=16)),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='my_lower',
            field=models.ForeignKey(to='app.Lower'),
            preserve_default=True,
        ),
    ]
