from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment
from django.core.mail import send_mail
import os

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .models import Appointment

@login_required
def create_appointment(request):
    if request.user.user_type != 'company':
        return redirect('dashboard')

    if request.method == 'POST':
        form = AppointmentForm(request.POST, company=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.company = request.user
            appointment.save()

            if appointment.customer.email:
                send_mail(
                    subject='New Appointment Scheduled',
                    message=f'''
Hello {appointment.customer.username},

You have a new appointment with {appointment.company.username}.

Title: {appointment.title}
Date: {appointment.date}
Time: {appointment.time}
Notes: {appointment.notes or "None"}

Thanks,
Appointment Booking System
                    ''',
                    from_email=os.getenv("EMAIL_HOST_USER"),
                    recipient_list=[appointment.customer.email],
                    fail_silently=True,
                )

            return redirect('dashboard')
    else:
        form = AppointmentForm(company=request.user)

    return render(request, 'appointments/create_appointment.html', {'form': form})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, company=request.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment, company=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully.")
            return redirect('dashboard')
    else:
        form = AppointmentForm(instance=appointment, company=request.user)

    return render(request, 'appointments/create_appointment.html', {
        'form': form,
        'edit_mode': True
    })

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, company=request.user)

    if request.method == 'POST':
        appointment.delete()
        messages.success(request, "Appointment deleted.")
        return redirect('dashboard')

    return render(request, 'appointments/confirm_delete.html', {'appointment': appointment})



@login_required
def calendar_view(request):
    return render(request, 'appointments/calendar.html')

@login_required
def get_appointments_json(request):
    user = request.user
    if user.user_type == 'company':
        appointments = Appointment.objects.filter(company=user)
    else:
        appointments = Appointment.objects.filter(customer=user)

    events = []
    for a in appointments:
        events.append({
            'title': a.title,
            'start': f"{a.date}T{a.time}",
            'description': a.notes or "",
        })
    return JsonResponse(events, safe=False)