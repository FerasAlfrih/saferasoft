from django.db import models

# Create your models here.


class corona(models.Model):
    """docstring for corona"""

    country = models.CharField(max_length=100)
    totalcases = models.CharField(max_length=100)
    newcases = models.CharField(max_length=100)
    totaldeathes = models.CharField(max_length=100)
    newdeathes = models.CharField(max_length=100)
    totalrecovered = models.CharField(max_length=100)
    activecases = models.CharField(max_length=100)
    criticalcases = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.country)
