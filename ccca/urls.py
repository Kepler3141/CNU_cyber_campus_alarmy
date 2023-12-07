from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.main),
    path('notifications/', views.notifications),
    path('assignments/', views.assignments),
    path('materials/', views.materials)
]