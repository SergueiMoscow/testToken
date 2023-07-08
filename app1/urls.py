from django.urls import path

from app1 import views

urlpatterns = [
    path('protected', views.protected, name='protected'),
]