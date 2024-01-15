from django.shortcuts import render, HttpResponse
from .random_number import func_random_number

# Create your views here.
def home(request):
    return render(request, "home.html", {"number": func_random_number}) 