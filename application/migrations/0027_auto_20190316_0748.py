# Generated by Django 2.1.7 on 2019-03-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0026_remove_school_school_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.IntegerField(db_column='admission_number', help_text='Enter admission number', unique=True, verbose_name='Admission number'),
        ),
    ]
