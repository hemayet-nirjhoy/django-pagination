from django.http import Http404, HttpResponse
from django.shortcuts import render
from numpy import number
import pandas as pd
from .models import *
import pandas as pd
from django.core.paginator import Paginator


# Create your views here.
def books(request):
    try:
        return render(request, "books.html")
    except Exception as e:
        return Http404(str(e))

def customers(request):
    try:
        context = {}
        context['customers'] = Customer.objects.all()
        return render(request, 'customers.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))

def customersSimplePagination(request):
    try:
        offset = 10             # number of customer (row) per page
        customers = Customer.objects.all()
        paginator = Paginator(customers, offset)

        # Fetch the page no
        page_no = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_no)

        # Pagination button should have beautiful design
        page_range = paginator.get_elided_page_range(number=page_no)
        
        return render(request, 'customers.html',{'customers':page_obj, 'page_range':page_range})
    except Exception as e:
        return HttpResponse(str(e))

def autoAddCustomers(request):
    try:
        customers = pd.read_csv("customers.csv")
        print(customers.head)
        for _, row in customers.iterrows():
            print(row['first_name'])
            temp  = Customer.objects.create(
                first_name = row['first_name'],
                last_name = row['last_name'],
                email = row['email'],
                gender = row['gender'],
                ip = row['ip_address']
            )
            temp.save()
        return HttpResponse("Done!")
    except Exception as e:
        return HttpResponse(str(e))