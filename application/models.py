import datetime
from django.urls import reverse

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    """Model representing student."""

    first_name = models.CharField(
        "First name",
        max_length=200,
        help_text="Enter first name",
        db_column="first_name",
    )
    last_name = models.CharField(
        "Last name",
        max_length=200,
        help_text="Enter last name",
        db_column="last_name"
    )
    admission_number = models.PositiveSmallIntegerField(
        "Admission number",
        unique=True,
        help_text="Enter admission number",
        db_column="admission_number",
    )
    Date_of_Birth = models.DateField(
        "Date of birth",
        help_text="Enter date of birth",
        default="1998-02-02",
        db_column="date_of_birth",
    )
    current_class = models.IntegerField(
        "current class",
        help_text="Enter the student's current class",
        db_column="current_class",
    )
    school = models.ForeignKey(
        "School",
        on_delete=models.CASCADE,
        db_column="school")
    home_town = models.CharField(
        "Home town",
        max_length=200,
        help_text='Enter the location "County/Constituence/Town"',
        blank=True,
        db_column="home_town",
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["admission_number"]
        db_table = "students"

    def clean(self):
        # if  in primary school then  classes should 1-8
        if self.school.school_category == "PRI_SCH":
            if self.current_class <= 0 or self.current_class > 8:
                raise ValidationError(_("Class 1-8"))
        if self.school.school_category == "SEC_SCH":
            if self.current_class <= 0 or self.current_class > 4:
                raise ValidationError(_("Form 1-4"))

        if self.Date_of_Birth >= datetime.date.today():
            raise ValidationError(_("Invalid Date of Birth. Date too small"))

        if self.Date_of_Birth <= datetime.date(1997, 1, 1):
            raise ValidationError(_("Invalid date of birth. Date too large"))


class Parent(models.Model):
    first_name = models.CharField(
        "First name",
        max_length=200,
        help_text="Enter first name",
        db_column="first_name",
    )
    last_name = models.CharField(
        "Last name", max_length=200,
        help_text="Enter last name",
        db_column="last_name"
    )
    email_address = models.EmailField(
        max_length=254, help_text="Enter email address.",
        db_column="email_address"
    )
    student = models.ManyToManyField(
        "Student", help_text="students names", db_column="student"
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["last_name", "first_name"]
        db_table = "parents"


class School(models.Model):
    school_name = models.CharField(
        "School name",
        max_length=200,
        help_text="Enter last name",
        db_column="school_name",
    )
    number_of_teachers = models.IntegerField(
        "Number of Teachers in School",
        help_text="Enter the number of teaching stuff",
        default=40,
        db_column="number_of_teachers",
    )
    number_of_students = models.IntegerField(
        "Total students",
        help_text="Enter the total number of students",
        default=200,
        db_column="number_of_students",
    )
    school_location = models.CharField(
        "School Location",
        max_length=200,
        help_text='Enter "County/Constituence/Town"',
        blank=True,
        db_column="school_location",
    )
    year_established = models.DateField(
        "Date Established",
        help_text="Enter the date in which school was established",
        default="01/01/2000",
        db_column="year_established",
    )
    SCHOOL_CATEGORY = (
        ("PRI_SCH", "Primary School"), ("SEC_SCH", "Secondary School")
        )
    school_category = models.CharField(
        "School level",
        help_text="Select school level",
        choices=SCHOOL_CATEGORY,
        default="SEC_SCH",
        max_length=20,
        db_column="school_category",
    )
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True, blank=True)

    def get_absolute_url(self):
        return reverse("school", kwargs={"pk": self.pk})

    def __str__(self):
        return self.school_name

    class Meta:
        db_table = "schools"
        ordering = [
            "school_category", "number_of_students", "number_of_teachers"
            ]
