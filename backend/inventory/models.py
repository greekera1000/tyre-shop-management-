from django.db import models
from tyres.models import Tyre

class Stock(models.Model):
    tyre = models.ForeignKey(Tyre, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tyre.brand} - {self.quantity}"
