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


class worldCountries(models.Model):
    name = models.CharField(max_length=100)
    arname = models.CharField(max_length=100, default="")
    dename = models.CharField(max_length=100, default="")
    frname = models.CharField(max_length=100, default="")
    grname = models.CharField(max_length=100, default="")
    esname = models.CharField(max_length=100, default="")
    runame = models.CharField(max_length=100, default="")
    code = models.CharField(max_length=2)
    call = models.CharField(max_length=4, default="0")

    def __str__(self):
        return (self.name)


class arabicCountries(models.Model):
    name = models.CharField(max_length=100)
    dename = models.CharField(max_length=100, default="")
    frname = models.CharField(max_length=100, default="")
    grname = models.CharField(max_length=100, default="")
    esname = models.CharField(max_length=100, default="")
    runame = models.CharField(max_length=100, default="")
    code = models.CharField(max_length=2)
    call = models.CharField(max_length=4)

    def __str__(self):
        return (self.code)
