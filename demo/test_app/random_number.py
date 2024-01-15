import random
from django.http import JsonResponse

def func_random_number(request):
    number = random.randint(1, 100)
    return JsonResponse({'number': number})

