from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation


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


def contact(request):
    person = PersonalInformation.objects.first()

    return render(request, 'contact.html', {
        'person': person
    })