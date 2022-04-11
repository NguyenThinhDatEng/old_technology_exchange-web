from django.urls import path

from .views import GetAllCustomer, Create

urlpatterns = [
    path('customers/', GetAllCustomer.as_view(), name='customers'),
    path('customers/create/', Create.as_view(), name='create'),
]
