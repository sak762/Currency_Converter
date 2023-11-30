from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
