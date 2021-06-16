from django.urls import path, include
from . import views
from .views import OrderUpdateView
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
	path('',views.place_order, name = "place_order"),
	path('pay/',views.gateway, name = 'gateway'),
    path('pay/success/',views.success, name = 'success'),
    path('order/<int:pk>/', OrderUpdateView.as_view(), name = 'order-update'),
    path('corders', views.customer, name='customer-orders'),
    path('orders', views.shopkeeper, name='shopkeeper-orders'),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name = 'download'),
    url(r'^change/(?P<path>.*)$',views.status_change,name = 'change'),
    url(r'^valid/(?P<path>.*)$',views.validator,name = 'valid'),
]