from django.urls import path

from .views import addToOrder, viewOrder, removeFromCart

urlpatterns = [
    path('addToOrder/<int:id>-<int:quantity>/', addToOrder, name='addToOrder'),
    path('', viewOrder, name='viewOrder'),
    path('removeFromCart/<int:id>/', removeFromCart, name='removeFromCart'),

]