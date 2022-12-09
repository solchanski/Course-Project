from django.urls import path

from booking_tickets import views

urlpatterns = [
    path('sign_up/', views.CreateAccountView.as_view(), name="sign_up"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('personal_account/', views.PersonalAccountView.as_view(), name="personal_account"),
    path('available_tickets/', views.AvailableTicketsView.as_view(), name="available_tickets"),
    path('ordering/', views.OrderingView.as_view(), name="ordering")
]
