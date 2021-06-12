from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Order
from .forms import PlaceOrderForm

def place_order(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.session['user'])
            username = request.session['user']['name']
            neworder = Order(customer = username,docfile = request.FILES['docfile'])
            neworder.save()
            messages.success(request,f'Your order has been placed.')
            return redirect('home')
    else : 
        form = PlaceOrderForm()
        key = 'user'
        if key in request.session:
            return render(request,'task/place_order.html',{'form':form, 'user': request.session[key]}) 
        else:
            return redirect('home')