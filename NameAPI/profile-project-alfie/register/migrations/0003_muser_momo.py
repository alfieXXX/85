# Generated by Django 3.2.9 on 2022-02-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20220218_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='momo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
