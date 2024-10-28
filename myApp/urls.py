from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('profil/', views.profil, name='profil'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
]
