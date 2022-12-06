from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Company(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Bus(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', default=0)
    bus_number = models.CharField(max_length=6)
    bus_type = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    seats = models.IntegerField(default=20)

    def __str__(self):
        return str(self.bus_type + ' ' + self.bus_number)


class Location(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return str(f"{self.city}, {self.country}")


class Route(models.Model):
    departure_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name="Departure location",
        related_name="departure"
    )
    arrival_location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name="Arrival location",
        related_name="arrival"
    )

    def __str__(self):
        return str(f"{self.departure_location} - {self.arrival_location}")


class Ticket(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route', default=0)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='route', default=0)
    from_time = models.TimeField(default=timezone.now)
    to_time = models.TimeField(default=timezone.now)
    travel_time = models.CharField(max_length=10, default=0)
    price = models.FloatField(max_length=10, default=0)

    def __str__(self):
        return str(f"ROUTE: {self.route} TIME: {self.from_time} - {self.to_time} PRICE: {self.price} BYN")


class Date(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticket', default=0)
    available = models.DateField(default=timezone.now)

    def __str__(self):
        return str(f"{self.available} {self.ticket}")


class Order(models.Model):
    available_ticket = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='available_date', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=0)
    seat = models.IntegerField(default=0)

    def __str__(self):
        return str(f"{self.user} {self.seat}")
