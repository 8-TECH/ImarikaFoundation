from django.db import models
from django.utils import timezone

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} donated {self.amount} on {self.date}"

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    interest_area = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Event(models.Model):
    EVENT_TYPES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    location = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.name

    def is_upcoming(self):
        return self.event_type == 'upcoming' and self.event_date > timezone.now()

    def is_past(self):
        return self.event_type == 'past' and self.event_date < timezone.now()
