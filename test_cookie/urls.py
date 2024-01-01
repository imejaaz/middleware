from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_test_cookie),
    path('get/', views.check_test_cookie),
    path('delete/', views.delete_test_cookies),

]