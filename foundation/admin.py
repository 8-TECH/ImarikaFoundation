from django.contrib import admin

from .models import Event, Donation, Volunteer

admin.site.register(Donation)
admin.site.register(Event)
admin.site.register(Volunteer)