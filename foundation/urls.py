from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('donation-success/', views.donation_success, name='donation_success'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteer-success/', views.volunteer_success, name='volunteer_success'),
    # path('events/', views.event_list, name='event_list'),
    path('event/register/<int:event_id>/', views.event_register, name='event_register'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
