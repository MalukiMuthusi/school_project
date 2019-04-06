from django.shortcuts import render
from django.shortcuts import redirect

from application.models import School

# from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from .forms import SnippetForm, ContactForm, LoginForm
# import datetime
from django.views.generic.edit import CreateView

# DeleteView, UpdateView
# from django.views import generic
from .forms import SchoolRegisterForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


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
        "results": results,
    }
    return render(request, "school.html", context=context)


def all_schools(request):
    all_entries = School.objects.all()
    pri_sch = School.objects.filter(school_category="PRI_SCH")
    sec_sch = School.objects.filter(school_category="SEC_SCH")
    context = {"all_entries": all_entries, "primo": pri_sch, "sec": sec_sch}
    # page = request.GET.get('page', 1)
    # paginator = Paginator(all_entries, 5)
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
        "results": results,
    }
    return render(request, "about_school.html", context=context)


""" create a sign up view for school """


def signup(request):
    return render(request, "school_reg.html")


def register(request):
    if request.method == "POST":
        form = SchoolRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("index")
    else:
        form = SchoolRegisterForm()
    return render(request, "school_reg.html", {"form": form})


def school_reg(request):
    return render(request, "school_reg.html")


""" add a school """


class SchoolCreate(CreateView):
    model = School
    fields = "__all__"
