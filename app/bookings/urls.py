from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
] 