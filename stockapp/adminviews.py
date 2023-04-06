from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from stockapp.forms import StockForm
from stockapp.models import Customer, Stock


@login_required(login_url='login_view')
def admindashboard(request):
    return render(request, 'Admin1/Adminbase.html')


@login_required(login_url='login_view')
def view_customer(request):
    data = Customer.objects.all()
    return render(request, 'Admin1/Viewcustomer.html', {'data': data})


@login_required(login_url='login_view')
def add_stock(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stock')
    return render(request, 'Admin1/Addstocks.html', {'form': form})


@login_required(login_url='login_view')
def view_stock(request):
    data = Stock.objects.all()

    return render(request, 'Admin1/Viewstocks.html', {'data': data})


@login_required(login_url='login_view')
def delete(request, id):
    data = Stock.objects.get(id=id)
    data.delete()
    return redirect('view_stock')
