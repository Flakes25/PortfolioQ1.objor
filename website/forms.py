from django import forms
from .models import Project, Inquiry, Testimony


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

        widgets = {
            "project_name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "tech_stack": forms.TextInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
        }


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = "__all__"

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }