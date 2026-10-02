from django import forms
from .models import Project, Inquiry, Testimony, TechStack


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

        widgets = {
            "project_name": forms.TextInput(attrs={
                "placeholder": "Project Name"
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Project Description"
            }),

            "tech_stack": forms.TextInput(attrs={
                "placeholder": "Technology Used"
            }),

            "link": forms.URLInput(attrs={
                "placeholder": "Project Link"
            }),
        }


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name"
            }),

            "contact_number": forms.TextInput(attrs={
                "placeholder": "Contact Number"
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "Email Address"
            }),

            "address": forms.TextInput(attrs={
                "placeholder": "Address"
            }),

            "message": forms.Textarea(attrs={
                "placeholder": "Your Message"
            }),
        }

class TechStackForm(forms.ModelForm):

  class Meta:
    model = TechStack
    fields = ["name"]

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = "__all__"

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Full Name"
            }),

            "content": forms.Textarea(attrs={
                "placeholder": "Write your testimony..."
            }),
        }