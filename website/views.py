from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import (
    Project,
    PersonalInformation,
    Inquiry,
    Testimony,
)

from .forms import (
    ProjectForm,
    InquiryForm,
    TestimonyForm,
)

def home(request):
    return render(request, 'home.html')


def about(request):
    person = PersonalInformation.objects.first()

    return render(request, "about.html", {
        "person": person
    })


def projects(request):
    projects = Project.objects.all()

    return render(request, 'projects.html', {
        'projects': projects
    })


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    return render(request, "project_detail.html", {
        "project": project
    })

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("projects")

    else:
        form = ProjectForm()

    return render(request, "project_form.html", {
        "form": form
    })

def contact(request):
    person = PersonalInformation.objects.first()

    if request.method == "POST":
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact")

    else:
        form = InquiryForm()

    return render(request, "contact.html", {
        "person": person,
        "form": form
    })

def testimony_create(request):
    if request.method == "POST":
        form = TestimonyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("testimony_list")

    else:
        form = TestimonyForm()

    return render(request, "testimony_form.html", {
        "form": form
    })

class TestimonyListView(ListView):
    model = Testimony
    template_name = "testimony_list.html"
    context_object_name = "testimonies"

def testimony_detail(request, id):
    testimony = get_object_or_404(Testimony, id=id)

    return render(request, "testimony_detail.html", {
        "testimony": testimony
    })