from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexpage),
    path('sports',views.sportspage),
    path('politics',views.politicspage),
    path('technology',views.techpage),
    path('startup',views.startuppage),
    path('science',views.sciencepage),
    path('business',views.businesspage)
]