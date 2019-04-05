from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.views.generic import TemplateView

from application.models import Parent, School, Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, "index.html")


def school(request, pk):
    school_name = School.objects.get(pk=pk)

    if school_name.school_category == "PRI_SCH":
        results = "KCPE past results"
    elif school_name.school_category == "SEC_SCH":
        results = "KCSE past results"
    else:
        results = "Past Results unavailable"

    context = {
        "name": school_name,
        "year": School.year_established,
        "sch_level": School.school_category,
        "pk": pk,
        "results": results
    }
    return render(request, "school.html", context=context)


def all_schools(request):
    all_entries = School.objects.all()
    pri_sch = School.objects.filter(school_category="PRI_SCH")
    sec_sch = School.objects.filter(school_category="SEC_SCH")
    context = {
        "all_entries": all_entries,
        "primo": pri_sch,
        "sec": sec_sch
        }
    page = request.GET.get('page', 1)
    paginator = Paginator(all_entries, 5)
    return render(request, "all_schools.html", context=context)


def about_sch(request, pk):
    school_name = School.objects.get(pk=pk)
    sch_level = school_name.school_category
    if school_name.school_category == "PRI_SCH":
        results = "KCPE past results"
    elif school_name.school_category == "SEC_SCH":
        results = "KCSE past results"
    else:
        results = "Past Results unavailable"
    context = {
        "name": school_name,
        "year": School.year_established,
        "sch_level": sch_level,
        "pk": pk,
        "results": results
    }
    return render(request, "about_school.html", context=context)