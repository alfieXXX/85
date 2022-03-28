# Generated by Django 3.2.5 on 2021-10-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0004_auto_20210922_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listdetail',
            old_name='fullname',
            new_name='birthday',
        ),
        migrations.RemoveField(
            model_name='listdetail',
            name='bio',
        ),
        migrations.AddField(
            model_name='listdetail',
            name='contactNumber',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listdetail',
            name='firstName',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listdetail',
            name='lastName',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listdetail',
            name='sex',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='listdetail',
            name='address',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='listdetail',
            name='age',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]