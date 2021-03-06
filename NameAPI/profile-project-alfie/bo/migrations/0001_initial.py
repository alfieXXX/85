# Generated by Django 3.2.9 on 2022-03-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MReference',
            fields=[
                ('reference_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('reference_group', models.CharField(max_length=100)),
                ('reference_code', models.CharField(max_length=20)),
                ('reference_shortdesc', models.CharField(max_length=100)),
                ('reference_longdesc', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('reference_desc', models.CharField(max_length=500)),
                ('reference_groupcode', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('reference_tablestatus_id', models.BigIntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('addedby_user_id', models.BigIntegerField()),
                ('updatedby_user_id', models.BigIntegerField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
