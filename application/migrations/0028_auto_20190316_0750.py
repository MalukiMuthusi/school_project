# Generated by Django 2.1.7 on 2019-03-16 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0027_auto_20190316_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
