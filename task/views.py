from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Order
from .forms import PlaceOrderForm
from payment import urls

def place_order(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.session['user'])
            username = request.session['user']['name']
            starting_page = form.cleaned_data.get('starting_page')
            ending_page = form.cleaned_data.get('ending_page')
            no_of_copies = form.cleaned_data.get('no_of_copies')
            black_and_white = form.cleaned_data.get('black_and_white')
            num_pages = ending_page-starting_page+1
            if black_and_white:
                cost = num_pages*1
            else:
                cost = num_pages*5
            neworder = Order(customer = username,docfile = request.FILES['docfile'], starting_page = starting_page, ending_page = ending_page, no_of_copies = no_of_copies, black_and_white=black_and_white, cost = cost )
            neworder.save()
            return HttpResponseRedirect(reverse('gateway'))
    else : 
        form = PlaceOrderForm()
        key = 'user'
        if key in request.session:
            return render(request,'task/place_order.html',{'form':form, 'user': request.session[key]}) 
        else:
            return redirect('home')