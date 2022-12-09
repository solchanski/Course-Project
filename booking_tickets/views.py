from django.views.generic import DetailView, FormView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.models import User
from booking_tickets.forms import CreateAccountForm, LoginForm, AvailableTicketsForm, PersonalAccountForm, OrderingForm


from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import json
from django.http import HttpResponse


class CreateAccountView(FormView):
    form_class = CreateAccountForm
    template_name = "booking_tickets/sign_up.html"
    success_url = "/booking_tickets/"

    def form_valid(self, form):
        new_user = User(**form.cleaned_data)
        new_user.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = "booking_tickets/login.html"
    success_url = "/booking_tickets/"

    def form_valid(self, form):
        new_user = User(**form.cleaned_data)
        new_user.save()
        return super().form_valid(form)


class AvailableTicketsView(FormView):
    form_class = AvailableTicketsForm
    template_name = "booking_tickets/available_tickets.html"
    success_url = "/booking_tickets/"

    def form_valid(self, form):
        new_user = User(**form.cleaned_data)
        new_user.save()
        return super().form_valid(form)


class PersonalAccountView(FormView):
    form_class = PersonalAccountForm
    template_name = "booking_tickets/personal_account.html"
    success_url = "/booking_tickets/"

    def form_valid(self, form):
        new_user = User(**form.cleaned_data)
        new_user.save()
        return super().form_valid(form)


class OrderingView(FormView):
    form_class = OrderingForm
    template_name = "booking_tickets/ordering.html"
    success_url = "/booking_tickets/"

    def form_valid(self, form):
        new_user = User(**form.cleaned_data)
        new_user.save()
        return super().form_valid(form)



# def login_user(request):
#     logout(request)
#     resp = {"status": 'failed', 'msg': ''}
#     username = ''
#     password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 resp['status'] = 'success'
#             else:
#                 resp['msg'] = "Incorrect username or password"
#         else:
#             resp['msg'] = "Incorrect username or password"
#     return HttpResponse(json.dumps(resp), content_type='application/json')
#
#
# def logoutuser(request):
#     logout(request)
#     return redirect('/')
