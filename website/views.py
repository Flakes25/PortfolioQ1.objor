from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import (
    Project,
    PersonalInformation,
    Inquiry,
    Testimony,
)

from .forms import (
    ProjectForm,
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
    errors = {}
    data = {}

    # field name -> (label, max_length matching models.py)
    fields = {
        "first_name": ("First name", 100),
        "last_name": ("Last name", 100),
        "contact_number": ("Contact number", 20),
        "email": ("Email", 254),
        "address": ("Address", 255),
        "message": ("Message", None),
    }

    if request.method == "POST":
        for name, (label, max_len) in fields.items():
            value = request.POST.get(name, "").strip()
            data[name] = value

            if not value:
                errors[name] = f"{label} is required."
            elif max_len and len(value) > max_len:
                errors[name] = f"{label} must be {max_len} characters or fewer."

        if "email" not in errors:
            try:
                validate_email(data["email"])
            except ValidationError:
                errors["email"] = "Please enter a valid email address."

        if not errors:
            Inquiry.objects.create(**data)
            messages.success(request, "Thank you! Your inquiry has been sent.")
            return redirect("contact")

    return render(request, "contact.html", {
        "person": person,
        "errors": errors,
        "data": data,
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