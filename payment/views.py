from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import razorpay

from .models import Coffee
from django.views.decorators.csrf import csrf_exempt

def gateway(request):
	if request.method== "POST":
		name = request.POST.get("name")
		amount = int(request.POST.get("amount"))*100
		client = razorpay.Client(auth = ("rzp_test_aBF0M5yvtP4PDr", "lPodFzCQ4YXDa9l8XfYCfgB3"))
		payment = client.order.create({'amount':amount, 'currency': 'INR', 'payment_capture':'1'})
		print(payment)
		coffee = Coffee(name = name, amount = amount, payment_id = payment['id'])
		coffee.save()
		return render(request,'payment/index.html',{'payment':payment})

	return render(request,'payment/index.html')

@csrf_exempt
def success(request):
	if request.method == "POST":
		a = request.POST
		print(a)
		for key, val in a.items():
			if key == "razorpay_order_id":
				order_id = val
				break
		print("order_id ", order_id)
		user = Coffee.objects.filter(payment_id = order_id).first()
		print("user ",user)
		user.paid = True
		user.save()
		messages.success(request,f'Your order has been placed.')
	return render(request, 'payment/success.html')
