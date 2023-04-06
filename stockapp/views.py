from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from stockapp.forms import Loginform, CustomerForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def customer_registration(request):
    form1 = Loginform()
    form2 = CustomerForm()

    if request.method == 'POST':
        form1 = Loginform(request.POST)
        form2 = CustomerForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_customer = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()

            return redirect('login_view')

    return render(request, 'Customer/CustomerSignup.html', {'form1': form1, 'form2': form2})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindashboard')
            elif user.is_customer:
                print(user)
                return redirect('customer_dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')
