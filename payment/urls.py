from django.urls import path, include
from .views import gateway, success

urlpatterns = [
	path('',gateway, name = "gateway"),
	path('success/', success, name = "success")
]