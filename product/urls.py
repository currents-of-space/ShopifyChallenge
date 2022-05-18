from django.urls import path
from .views import productDetails,productUpload

urlpatterns = [
    path('product-details/<int:id>', productDetails, name='productDetails'),
    path('productrelease/', productUpload, name='productRelesase'),

]