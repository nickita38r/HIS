from django.urls import path

from .views import (
    BaseView,
    BarberView
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('barber/<str:slug>/', BarberView.as_view(), name='barber_detail'),
]