from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.place_order, name = "place_order"),
	path('pay/',views.gateway, name = 'gateway'),
    path('pay/success/',views.success, name = 'success')
]