from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
	"""docstring for products"""

	name = models.CharField(max_length=200)
	p_type = models.CharField(max_length=200)
	price = models.IntegerField()
	reservedTo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	url = models.CharField(max_length=200)
	dateCreated = models.DateField(auto_now_add=True)
	is_reversed = models.BooleanField(default=False)
	is_sold = models.BooleanField(default=False)

	def __str__(self):
		return self.name
	
	