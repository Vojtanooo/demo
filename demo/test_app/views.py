from django.shortcuts import render, HttpResponse
from .models import Get_battery_Data
from django.http import JsonResponse
import random

def func_random_number(request):
    number = random.randint(1, 100)
    return JsonResponse({'number': number})

def get_data_from_database(request):
    soc = Get_battery_Data.objects.all().order_by('-time_stamp')[0].state_of_charge
    actual_power = Get_battery_Data.objects.all().order_by('-time_stamp')[0].actual_power
    return JsonResponse({"soc": soc, "actual_power" : actual_power})
                         
def home(request): 
    return render(request, "home.html") 