# Generated by Django 2.1.7 on 2019-03-16 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0028_auto_20190316_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', help_text='Enter first name', max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(db_column='last_name', help_text='Enter last name', max_length=200, verbose_name='Last name')),
                ('email_address', models.EmailField(db_column='email_address', help_text='Enter email address.', max_length=254)),
            ],
            options={
                'db_table': 'parents',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(db_column='school_name', help_text='Enter last name', max_length=200, verbose_name='School name')),
                ('number_of_teachers', models.IntegerField(db_column='number_of_teachers', default=40, help_text='Enter the number of teaching stuff', verbose_name='Number of Teachers in School')),
                ('number_of_students', models.IntegerField(db_column='number_of_students', default=200, help_text='Enter the total number of students', verbose_name='Total students')),
                ('school_location', models.CharField(blank=True, db_column='school_location', help_text='Enter "County/Constituence/Town"', max_length=200, verbose_name='School Location')),
                ('year_established', models.DateField(db_column='year_established', default='01/01/2000', help_text='Enter the date in which school was established', verbose_name='Date Established')),
                ('school_category', models.CharField(choices=[('PRI_SCH', 'Primary School'), ('SEC_SCH', 'Secondary School')], db_column='school_category', default='SEC_SCH', help_text='Select school level', max_length=20, verbose_name='School level')),
            ],
            options={
                'db_table': 'schools',
                'ordering': ['school_category', 'number_of_students', 'number_of_teachers'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', help_text='Enter first name', max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(db_column='last_name', help_text='Enter last name', max_length=200, verbose_name='Last name')),
                ('admission_number', models.PositiveSmallIntegerField(db_column='admission_number', help_text='Enter admission number', unique=True, verbose_name='Admission number')),
                ('Date_of_Birth', models.DateField(db_column='date_of_birth', default='1998-02-02', help_text='Enter date of birth', verbose_name='Date of birth')),
                ('current_class', models.IntegerField(db_column='current_class', help_text="Enter the student's current class", verbose_name='current class')),
                ('home_town', models.CharField(blank=True, db_column='home_town', help_text='Enter the location "County/Constituence/Town"', max_length=200, verbose_name='Home town')),
                ('school', models.ForeignKey(db_column='school', on_delete=django.db.models.deletion.CASCADE, to='application.School')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['admission_number'],
            },
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.ManyToManyField(db_column='student', help_text='students names', to='application.Student'),
        ),
    ]
