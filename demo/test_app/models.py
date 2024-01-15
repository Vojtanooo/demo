from django.db import models

class RandomNumber(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
