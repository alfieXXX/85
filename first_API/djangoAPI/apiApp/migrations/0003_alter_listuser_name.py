# Generated by Django 3.2.5 on 2021-09-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_rename_user_listuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listuser',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
