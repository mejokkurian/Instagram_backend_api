# Generated by Django 3.2.7 on 2021-12-30 11:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='followers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
        migrations.AddField(
            model_name='myuser',
            name='followings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
    ]
