from django.db import models

class Tyre(models.Model):
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    tyre_type = models.CharField(max_length=20)  # TT / TL

    cost_price = models.FloatField()
    selling_price = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto 5% margin if selling price not provided
        if not self.selling_price:
            self.selling_price = self.cost_price * 1.05
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} - {self.size}"
