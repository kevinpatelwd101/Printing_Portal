from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from .models import Order
from .forms import PlaceOrderForm
import yaml
import msal
import os
import time
from tutorial.auth_helper import get_token_from_code
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
from tutorial import views as tutorial_views
# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])

#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('myapp.views.list'))
#     else:
#         form = DocumentForm() # A empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     return render_to_response(
#         'myapp/list.html',
#         {'documents': documents, 'form': form},
#         context_instance=RequestContext(request)
#     )

def place_order(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST, request.FILES)
        if form.is_valid():
            # result = get_token_from_code(request)
            # user = get_user(result['access_token'])
            # username = request.session['user'].name
            neworder = Order(customer = user.name,docfile = request.FILES['docfile'])
            neworder.save()
            return redirect('')
    else : 
        form = PlaceOrderForm()
    return render(request,'task/place_order.html',{'form':form}) 