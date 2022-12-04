from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import Sum

class NotEnoughMoneyException(Exception):
    pass

class NotEnoughMoneyException(Exception):
    pass

class Company(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Bus(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    bus_number = models.CharField(max_length=6)
    bus_type = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    seats = models.FloatField(max_length=5)

    def __str__(self):
        return self.bus_number


class Location(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class Route(models.Model):
    amount = models.IntegerField(verbose_name="Transactional amount", default=0)
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


class Ticket(models.Model):
    pass
#     code = models.CharField(max_length=100)
#     bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
#     depart = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='depart_location')
#     destination = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='destination')
#     schedule= models.DateTimeField()
#     fare= models.FloatField()
#
#     def __str__(self):
#         return str(self.code + ' - ' + self.bus.bus_number)
#
#     def count_available(self):
#         booked = Booking.objects.filter(schedule=self).aggregate(Sum('seats'))['seats__sum']
#         return self.bus.seats - booked
#
#
class Date(models.Model):
    pass
#     data =
#
#
class Order(models.Model):
    pass
#     code = models.CharField(max_length=100)
#     name = models.CharField(max_length=250)
#     schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
#     seats = models.IntegerField()
#     status = models.CharField(max_length=2, choices=(('1','Pending'),('2','Paid')), default=1)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.code + ' - ' + self.name)
#
#     def total_payable(self):
#         return self.seats * self.schedule.fare
#





