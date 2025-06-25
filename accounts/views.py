from django.shortcuts import render, redirect
from .forms import CompanySignUpForm, CustomerSignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from appointments.models import Appointment

def register_company(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after registration
    else:
        form = CompanySignUpForm()
    return render(request, 'accounts/register.html', {'form': form, 'type': 'Company'})

def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'accounts/register.html', {'form': form, 'type': 'Customer'})

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def dashboard(request):
    if request.user.user_type == 'company':
        appointments = Appointment.objects.filter(company=request.user).order_by('date', 'time')
        return render(request, 'accounts/company_dashboard.html', {'appointments': appointments})
    
    elif request.user.user_type == 'customer':
        appointments = Appointment.objects.filter(customer=request.user).order_by('date', 'time')
        return render(request, 'accounts/customer_dashboard.html', {'appointments': appointments})

    else:
        return HttpResponseForbidden("Invalid user type")

def test_template(request):
    return render(request, 'base.html')
