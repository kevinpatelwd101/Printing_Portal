from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.urls import reverse

class Order(models.Model):
	customer = models.CharField(max_length = 100)
	docfile = models.FileField(default = 'blank.pdf', upload_to = 'order_pdf')
	date_ordered = models.DateTimeField(default = timezone.now)
	payment_status = models.BooleanField(default = False)
	printing_status = models.BooleanField(default = False)
	cost = models.IntegerField(default = 0)

	def __str__(self):
			return self.customer
