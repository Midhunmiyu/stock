from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from stockapp.models import Stock


@login_required(login_url='login_view')
def customer_dashboard(request):
    return render(request, 'Customer/Customerbase.html')


@login_required(login_url='login_view')
def customer_View_stocks(request):
    data = Stock.objects.all().order_by('-id')
    return render(request, 'Customer/Viewstocks.html', {'data': data})
