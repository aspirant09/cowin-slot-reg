# Generated by Django 3.1.7 on 2021-05-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0005_auto_20210508_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='district',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='pinCode',
            field=models.CharField(blank=True, default='00000', max_length=6),
        ),
    ]
