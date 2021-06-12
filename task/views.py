from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Order
from .forms import PlaceOrderForm
import razorpay

# from .models import Coffee
from django.views.decorators.csrf import csrf_exempt

def place_order(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.session['user'])
            username = request.session['user']['name']
            email = request.session['user']['email']
            starting_page = form.cleaned_data.get('starting_page')
            ending_page = form.cleaned_data.get('ending_page')
            no_of_copies = form.cleaned_data.get('no_of_copies')
            black_and_white = form.cleaned_data.get('black_and_white')
            num_pages = ending_page-starting_page+1
            price_black_and_white = 1
            price_color = 5
            if black_and_white:
                cost = num_pages*price_black_and_white
                cost = cost*no_of_copies
            else:
                cost = num_pages*price_color
                cost = cost*no_of_copies
            neworder = Order(customer = username, email = email,docfile = request.FILES['docfile'], starting_page = starting_page, ending_page = ending_page, no_of_copies = no_of_copies, black_and_white=black_and_white, cost = cost )
            neworder.save()
            return HttpResponseRedirect(reverse('gateway'))
    else : 
        form = PlaceOrderForm()
        key = 'user'
        if key in request.session:
            return render(request,'task/place_order.html',{'form':form, 'user': request.session[key]}) 
        else:
            return redirect('home')


def gateway(request):
    if request.method== "POST":
        email = request.session['user']['email']
        order = Order.objects.filter(email = email).last()
        cost = order.cost*100
        client = razorpay.Client(auth = ("rzp_test_aBF0M5yvtP4PDr", "lPodFzCQ4YXDa9l8XfYCfgB3"))
        payment = client.order.create({'amount':cost, 'currency': 'INR', 'payment_capture':'1'})
        print(payment)
        order.payment_id = payment['id']
        order.save()
        return render(request,'task/index.html',{'payment':payment})

    return render(request,'task/index.html')

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
        user = Order.objects.filter(payment_id = order_id).first()
        print("user ",user)
        user.payment_status = True
        user.save()
        messages.success(request,f'Your order has been placed.')
    return render(request, 'task/success.html')
