# Generated by Django 2.1.7 on 2019-03-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20190313_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='school_id',
        ),
        migrations.AddField(
            model_name='school',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
