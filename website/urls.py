from django.urls import path
from . import views

urlpatterns = [

    # Home
    path("", views.home, name="home"),

    # About
    path("about/", views.about, name="about"),

    # Projects
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id>/", views.project_detail, name="project_detail"),
    path("projects/add/", views.project_create, name="project_create"),

    # Contact / Inquiry
    path("contact/", views.contact, name="contact"),

    # Testimonies
    path("testimonies/", views.TestimonyListView.as_view(), name="testimony_list"),
    path("testimonies/add/", views.testimony_create, name="testimony_create"),
    path("testimonies/<int:id>/", views.testimony_detail, name="testimony_detail"),

    # Admin / Authentication
    path("login/", views.admin_login, name="admin_login"),
    path('logout/', views.admin_logout, name='admin_logout'),

    # --- NEW DASHBOARD & CREATE PATHS ---
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "dashboard/projects/create/",
        views.create_project_view,
        name="create_project",
    ),
    path(
        "dashboard/tech-stacks/create/",
        views.create_tech_stack_view,
        name="create_tech_stack",
    ),
]