
from django.contrib import admin

# Register your models here.
from .models import Parent, School, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'admission_number',
              'Date_of_Birth', 'current_class', 'school', 'home_town')
    search_fields = ['admission_number']
    list_filter = ('school', 'current_class', 'Date_of_Birth', 'home_town')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('school_name', ('number_of_teachers', 'number_of_students'),
              'school_location', 'year_established', 'school_category')
    search_fields = ['school_ID_Number', 'school_name']
    list_filter = ('school_category', 'school_location',
                   'number_of_students', 'number_of_teachers')


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'email_address', 'student')
    list_filter = ('student',)
    search_fields = ['first_name', 'last_name']
