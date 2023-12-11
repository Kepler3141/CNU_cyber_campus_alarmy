from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', views.signup, name='login'),
    path('signup/', views.signup, name='signup'),
]