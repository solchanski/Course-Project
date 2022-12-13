import datetime
from django.views.generic import FormView
from django.shortcuts import render
from booking_tickets.forms import *


class SearchTicketsView(FormView):
    form_class = SearchTicketsForm
    template_name = "index.html"
    success_url = "/booking_tickets/available_tickets"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def index(request):
        return render(request, "index.html")
