# Generated by Django 3.1.7 on 2021-05-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0003_auto_20210508_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='pinCode',
            field=models.CharField(default='1', max_length=6),
        ),
    ]