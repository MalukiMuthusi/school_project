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
    context = {
        "name": school_name,
        "year": School.year_established,
        "sch_level": School.school_category,
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

