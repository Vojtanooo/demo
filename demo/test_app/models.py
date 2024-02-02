from django.db import models

class RandomNumber(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Get_battery_Data(models.Model):
    actual_power = models.FloatField()
    state_of_charge = models.FloatField()
    time_stamp = models.DateTimeField(auto_now_add=True)
