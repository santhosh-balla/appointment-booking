from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_appointment, name='create_appointment'),
    path('edit/<int:pk>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/events/', views.get_appointments_json, name='calendar_events'),
]
