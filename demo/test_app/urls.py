from django.urls import path
from . import views
from .random_number import func_random_number

urlpatterns = [
    path("", views.home, name="home"),
    path('get_random_number/', func_random_number, name='get_random_number')
]