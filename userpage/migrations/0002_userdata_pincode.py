# Generated by Django 3.1.7 on 2021-05-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='pinCode',
            field=models.CharField(default='0', max_length=6),
        ),
    ]
