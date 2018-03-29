from django.urls import path

from . import views

urlpatterns = [
    path('substract', views.substract, name='substract'),
]