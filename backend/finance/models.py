from django.db import models

# Create your models here.
from django.db import models
from billing.models import Bill

class CreditRecord(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    total_amount = models.FloatField()
    paid_amount = models.FloatField(default=0)

    is_paid = models.BooleanField(default=False)

    def remaining_amount(self):
        return self.total_amount - self.paid_amount
