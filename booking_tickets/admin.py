from django.contrib import admin
from booking_tickets.models import Company, Bus, Location, Route, Ticket, Date, Order


admin.site.register(Company)
admin.site.register(Bus)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(Ticket)
admin.site.register(Date)
admin.site.register(Order)


