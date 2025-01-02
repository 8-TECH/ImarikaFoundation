from django.shortcuts import render, redirect
from .forms import DonationForm, VolunteerForm, EventRegistrationForm
from .models import Donation, Volunteer, Event
from django.http import HttpResponse


def home(request):
    return render(request, 'foundation/home.html')

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_success')
    else:
        form = DonationForm()
    return render(request, 'foundation/donate.html', {'form': form})

def donation_success(request):
    return render(request, 'foundation/donation_success.html')

def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_success')
    else:
        form = VolunteerForm()
    return render(request, 'foundation/volunteer.html', {'form': form})

def volunteer_success(request):
    return render(request, 'foundation/volunteer_success.html')



def home(request):
    upcoming_events = Event.objects.filter(event_type='upcoming').order_by('event_date')
    past_events = Event.objects.filter(event_type='past').order_by('-event_date')
    
    return render(request, 'foundation/home.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    })

def event_register(request, event_id):
    event = Event.objects.get(id=event_id)
    
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            # You can save the registration details to a new model or send them via email
            # Here we'll simply redirect to a success page
            return redirect('registration_success')
    else:
        form = EventRegistrationForm()

    return render(request, 'foundation/event_register.html', {
        'event': event,
        'form': form,
    })

def registration_success(request):
    return render(request, 'foundation/registration_success.html')
