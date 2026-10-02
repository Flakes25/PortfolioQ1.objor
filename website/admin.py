from django.contrib import admin
from .models import Inquiry, Project, PersonalInformation, Testimony, TechStack

admin.site.register(Project)
admin.site.register(PersonalInformation)
admin.site.register(Inquiry)
admin.site.register(Testimony)
admin.site.register(TechStack)

