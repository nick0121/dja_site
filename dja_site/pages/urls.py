from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('company/', views.company, name="company"),
    path('industries/', views.industries, name="industries"),
    path('contact/', views.contact, name="contact"),
    path('technology/', views.technology, name="technology"),
]