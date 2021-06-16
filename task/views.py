from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Order
from .forms import PlaceOrderForm
from .forms import otpForm
from django.views.generic import UpdateView
import razorpay
import random
from PyPDF2 import PdfFileMerger
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from reportlab.pdfgen import canvas 
from reportlab.pdfbase import pdfmetrics
import os

def customer(request):
    email = request.session['user']['email']
    all_entries = Order.objects.filter(customer_email = email , collected_status= False)
    return render(request, 'task/c_display.html', {'all_entries' : all_entries})

# quering into the database to find out the orders reamining to be printed by the shopkeeper
def shopkeeper(request):
       form = otpForm()
       email = request.session['user']['email']
       all_entries = Order.objects.filter(collected_status = False)
       return render(request, 'task/display.html', {'all_entries':all_entries ,'form' :form})

def place_order(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST, request.FILES)
        if form.is_valid():
            customer_name = request.session['user']['name']
            customer_email = request.session['user']['email']
            
            no_of_copies = form.cleaned_data.get('no_of_copies')
            black_and_white = form.cleaned_data.get('black_and_white')
            otp = random.randint(1000,10000)

            #creating extra pdf having name and email
            os.chdir(settings.MEDIA_ROOT)
            extrahash = random.randint(10000,100000)
            fileName = str(extrahash)+'temporary.pdf'
            title = customer_name
            subTitle = customer_email
            pdf = canvas.Canvas(fileName)
            pdf.setFont("Courier-Bold", 36)
            pdf.drawCentredString(300, 590, title)
            pdf.setFont("Courier-Bold", 24)
            pdf.drawCentredString(290,500, subTitle)
            pdf.save()

            # pdf merging
            files = request.FILES.getlist('docfile')
            merger = PdfFileMerger()
            for items in files:
                merger.append(items)
            pdfname = random.randint(10000,100000)
            newfile_name = customer_email + str(pdfname) + '.pdf'
            merger.append(fileName)
            merger.write(newfile_name)
            num_pages = len(merger.pages)
            merger.close

            #calculating cost
            price_black_and_white = 1
            price_color = 5
            if black_and_white:
                cost = num_pages*price_black_and_white
            else:
                cost = num_pages*price_color
            cost = cost*no_of_copies

            neworder = Order(customer_name = customer_name, customer_email = customer_email, otp = otp, 
                docfile = newfile_name,  no_of_copies = no_of_copies, black_and_white=black_and_white, 
                cost = cost)
            neworder.save()
            return HttpResponseRedirect(reverse('gateway'))
    else : 
        form = PlaceOrderForm()
        key = 'user'
        if key in request.session:
            return render(request,'task/place_order.html',{'form':form, 'user': request.session[key]}) 
        else:
            return redirect('home')


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['printing_status']



def gateway(request):
    if request.method== "POST":
        email = request.session['user']['email']
        order = Order.objects.filter(customer_email = email).last()
        cost = order.cost*100
        client = razorpay.Client(auth = ("rzp_test_aBF0M5yvtP4PDr", "lPodFzCQ4YXDa9l8XfYCfgB3"))
        payment = client.order.create({'amount':cost, 'currency': 'INR', 'payment_capture':'1'})
        order.payment_id = payment['id']
        order.save()
        return render(request,'task/index.html',{'payment':payment})
    return render(request,'task/index.html')

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print(request.session['user']['email'])
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        user = Order.objects.filter(payment_id = order_id).first()
        user.payment_status = True
        user.save()
        messages.success(request,f'Your order has been placed.')
    return render(request, 'task/success.html')

#class based function expect views of the following naming convertion:
# <app>/<model>_<viewtype>.html

# but for update it expects name to be <app>/<model>_form.html 
# because it shares the template with create view



def download(request, path):
    file_path = path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
    
def status_change(request,path):
    transaction = Order.objects.filter(payment_id = path)
    transaction.printing_status = True
    transaction.update(printing_status= True)
    return redirect('shopkeeper-orders')

def validator(request,path):
    form = otpForm(request.POST)
    if form.is_valid() :
           data = form.cleaned_data
           otp = data['otp']
           transaction = Order.objects.get(payment_id = path)
           tras = Order.objects.filter(payment_id=path)
           if transaction.otp == otp:
                 tras.update(collected_status=True)
                 return redirect('shopkeeper-orders')
           else :
               return redirect('shopkeeper-orders')