from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import ObjectDoesNotExist

from django.contrib.auth.models import User
from booking_tickets.models import Company, Bus, Location, Route, Ticket, Date, Order
from django.views.generic import FormView

class SignUpView(FormView):
    pass
    # form_class = ''
    # template_name = 'signup.html'
    # success_url = ''

    def form_valid(self, form):
        pass