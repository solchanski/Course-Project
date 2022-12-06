from django.contrib import admin
from booking_tickets.models import Company, Bus, Location, Route, Ticket, Date, Order


class DateAdmin(admin.ModelAdmin):
    list_display = ["available", "ticket"]
    list_filter = ["available"]


class TicketAdmin(admin.ModelAdmin):
    list_display = ["route", "from_time", "to_time", "price"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "available_ticket", "seat"]
    list_filter = ["user"]


admin.site.register(Company)
admin.site.register(Bus)
admin.site.register(Location)
admin.site.register(Route)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Order, OrderAdmin)


