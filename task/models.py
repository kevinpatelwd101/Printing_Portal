from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.urls import reverse

class Order(models.Model):
	customer = models.CharField(max_length = 100)
	email = models.CharField(default = 'hello@iitg.ac.in', max_length = 100)
	docfile = models.FileField(default = 'blank.pdf', upload_to = '')
	payment_id = models.CharField(default = '0000000000', max_length=100)
	date_ordered = models.DateTimeField(default = timezone.now)
	payment_status = models.BooleanField(default = False)
	printing_status = models.BooleanField(default = False)
	starting_page = models.IntegerField(default = 1)
	ending_page = models.IntegerField(default = 1)
	no_of_copies = models.IntegerField(default = 1)
	black_and_white = models.BooleanField(default = True)
	cost = models.IntegerField(default = 1)

	def __str__(self):
			return self.customer
