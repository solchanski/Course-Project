from django.views.generic import DetailView, FormView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.views import LoginView
from booking_tickets.forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import request, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


class CreateAccountView(FormView):
    form_class = CreateAccountForm
    template_name = "registration/sign_up.html"
    success_url = "/booking_tickets/login"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = LoginForm
    template_name: "registration/login.html"

    def get_success_url(self):
        return reverse('index')


class PersonalAccountView(ListView, LoginRequiredMixin):
    model = Order
    template_name = "booking_tickets/personal_account.html"
    success_url = "/booking_tickets/personal_account"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        u = self.request.user
        orders = Order.objects.filter(user=u).select_related("available_ticket").all()
        context['orders'] = orders
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)
        return queryset


class DeleteOrderView(DeleteView):
    model = Order
    template_name = "booking_tickets/order_delete.html"
    success_url = '/'


class AvailableTicketsView(ListView, LoginRequiredMixin):
    model = Order
    template_name = "booking_tickets/available_tickets.html"
    success_url = "/booking_tickets/personal_account"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tickets = Date.objects.select_related("ticket").all()
        context['tickets'] = tickets
        return context
