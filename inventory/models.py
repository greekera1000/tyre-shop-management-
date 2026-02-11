from django.db import models
from tyres.models import Tyre

class Stock(models.Model):
    tyre = models.ForeignKey(Tyre, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)
