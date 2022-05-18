from django.db import models
# from product.models import Product
from .infrastructure.modeldate import ModelDate

# # Create your models here.
# class DeliveryAddress(models.Model):
#     """
#     Stores a delivery address of the order.
#     """
#     firstName = models.CharField(max_length=150, blank=False, help_text="First name of a purchaser.")
#     lastName = models.CharField(max_length=150, blank=False, help_text="Last name of a purchaser.")
#     email = models.EmailField(blank=False, help_text="E-mail address of a purchaser. An order confirmation is sent to this e-mail address.")
#
# class Order(ModelDate):
#     """
#     Represents a user order.
#     """
#     deliveryAddress = models.ForeignKey(DeliveryAddress, on_delete=models.DO_NOTHING, help_text="Delivery address of the order.")
#     isConfirmed = models.BooleanField(default=False, help_text="Indicates if the order is confirmed.")
#
# class OrderElement(models.Model):
#     """
#     Represents an order's element
#     """
#     product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, help_text="Order element.")
#     quantity = models.IntegerField(help_text="Quantity of elements.")
#     order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, help_text="Associated order.")