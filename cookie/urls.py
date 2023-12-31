from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('set/', views.set),
    path('get/', views.get),
    path('delete/', views.delete),
]