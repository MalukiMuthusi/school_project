# Generated by Django 2.1.7 on 2019-03-16 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0025_auto_20190316_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='school_ID_Number',
        ),
    ]
