from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # About
    path('about/', views.about, name='about'),

    # Projects
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
    path('projects/add/', views.project_create, name='project_create'),

    # Contact / Inquiry
    path('contact/', views.contact, name='contact'),

    # Testimonies
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.testimony_create, name='testimony_create'),
    path('testimonies/<int:id>/', views.testimony_detail, name='testimony_detail'),
]