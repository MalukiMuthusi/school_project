# Generated by Django 2.1.7 on 2019-03-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0017_auto_20190313_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.AutoField(db_column='parent_id', help_text='This the parent unique id', primary_key=True, serialize=False, verbose_name='Parent ID')),
                ('first_name', models.CharField(db_column='first_name', help_text='Enter first name', max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(db_column='last_name', help_text='Enter last name', max_length=200, verbose_name='Last name')),
                ('email_address', models.EmailField(db_column='email_address', help_text='Enter email address.', max_length=254)),
                ('student', models.ManyToManyField(db_column='student', help_text='students names', to='application.Student')),
            ],
            options={
                'db_table': 'parents',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]