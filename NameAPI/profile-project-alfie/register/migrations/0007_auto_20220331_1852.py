# Generated by Django 3.2.9 on 2022-03-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_alter_muser_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='muser',
            name='lastname',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
