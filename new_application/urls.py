from django.http.response import HttpResponse
from django.urls import path, include
from . import views

app_name = 'account_application_form'
urlpatterns = [
    path('hello/', views.new_application, name='new_application'),
    path('approved/', views.approved, name='approved'),    
]