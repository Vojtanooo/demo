from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('get_random_number/', views.func_random_number, name='get_random_number'),
    path('get_data_from_database/', views.get_data_from_database, name='get_data_from_database'),
]