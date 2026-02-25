

# Create your models here.
from django.db import models
from tyres.models import Tyre

class Bill(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)

    tyre = models.ForeignKey(Tyre, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    selling_price = models.FloatField()
    total_amount = models.FloatField()

    payment_type = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)
