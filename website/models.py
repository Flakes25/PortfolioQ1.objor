from django.db import models


class TechStack(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.ForeignKey(TechStack, on_delete=models.CASCADE)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

    @property
    def truncated_description(self):
        if len(self.description) > 50:
            return self.description[:50] + "..."
        return self.description

    @property
    def tech_stack_comma_separated(self):
        return self.tech_stack.name if self.tech_stack else ""


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Testimony(models.Model):
    full_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.full_name