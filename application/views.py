from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from application.models import School, Student

# from django.contrib.auth.models import User

# from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from .forms import SnippetForm, ContactForm, LoginForm
# import datetime
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# DeleteView, UpdateView
# from django.views import generic
from .forms import SchoolRegisterForm, request_dataForm
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


""" Use Class list view """


class SchoolListView(ListView):
    model = School
    template_name = "all_schools.html"


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
            return redirect("school_login", permanent=True)
    else:
        form = SchoolRegisterForm()
    return render(request, "school_reg.html", {"form": form})


def school_reg(request):
    return render(request, "school_reg.html")


""" add a school """


class SchoolCreate(CreateView):
    model = School
    fields = "__all__"


""" Login Redirect view """


@login_required
def login_redirect(request):
    # pk = user.school.pk
    # if it is a school admin accout
    try:
        return redirect(request.user.school, permanent=True)
    except:
        return redirect("index", permanent=True)


""" Request for student data """


@login_required
def request_data(request, pk):
    if request.method == "POST":
        form = request_dataForm(request.POST)
        if form.is_valid():
            admn = form.cleaned_data.get("Admn")
            schn = form.cleaned_data.get("school")
            sch = schn.pk
            return redirect("view_data", admn, sch, permanent=True)
    else:
        form = request_dataForm()
    name = School.objects.get(pk=pk)
    context = {"form": form, "pk": pk, "name": name}
    return render(request, "request-data.html", context=context)


""" View data """


@login_required
def view_data(request, admn, sch):
    # sch_name = School.objects.get(pk=sch)
    # student = sch_name.objects.filter(Student=admn)

    try:
        student = Student.objects.get(
            admission_number=admn, school=School.objects.get(pk=sch)
        )
        context = {
            "first_name": student.first_name,
            "last_name": student.last_name,
            "DOB": student.Date_of_Birth,
            "class": student.current_class,
            "pk": sch,
            "name": School.objects.get(pk=sch),
            "student": student
        }
        return render(request, "view_data.html", context=context)
    except:
        user = request.user
        school = School.objects.get(user=user)
        context = {"pk": school.pk, "name": school}
        return render(request, "error_403.html", context)
