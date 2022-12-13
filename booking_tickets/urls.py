from django.urls import path

from booking_tickets import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('sign_up/', views.CreateAccountView.as_view(), name="sign_up"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name="logout"),
    path('personal_account/', views.PersonalAccountView.as_view(), name="personal_account"),
    path('personal_account/<int:pk>', views.DeleteOrderView.as_view(), name='delete_order'),
    path('available_tickets/', views.AvailableTicketsView.as_view(), name="available_tickets"),
    path('available_tickets/<int:pk>', views.AvailableTicketsView.as_view(), name="create_order"),
]
