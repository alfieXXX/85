# Generated by Django 3.2.9 on 2022-04-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rafflePeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('lastName', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, default='', null=True)),
                ('birthday', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('sex', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('contactNumber', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('lokal', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('data_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
