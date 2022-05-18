from django.db import models

# class Product(models.Model):
#     Name = models.CharField(max_length=100)
#     Category = models.CharField(max_length=100)
#     Price = models.DecimalField(max_digits=19, decimal_places=2)
#     Description = models.CharField(max_length=10000)
#     Picture = models.CharField(max_length=300)
#     IsOnSale = models.BooleanField()
#     IsAvailable = models.BooleanField()
#
# FILTER_CHOICES = (
#     ('Name', 'Name ascending'),
#     ('-Name', 'Name descending'),
#     ('Price', 'Price ascending'),
#     ('-Price', 'Price descending'),
#     ('Category', 'Category ascending'),
#     ('-Category', 'Category descending')
# )
#
# class FilterProduct(models.Model):
#     filterChoice = models.CharField(max_length=25 ,choices=FILTER_CHOICES, default='Name')
#     isOnSale = models.BooleanField()
#     isAvailable = models.BooleanField()
