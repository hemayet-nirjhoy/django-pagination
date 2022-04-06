from django.urls import path 
from .views import *

urlpatterns = [
    path('books/', books, name="books"),
    path('customers/', customers, name="customers"),  # simple view 
    path('customers-page/', customersSimplePagination, name="customers"),  # simple view 
    # path('add-customer/', autoAddCustomers, name="adding-customer"),
]
