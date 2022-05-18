# from django.forms import ModelForm
# from django import forms
# from .models import DeliveryAddress
#
# class DeliveryAddressForm(ModelForm):
#     class Meta:
#         model = DeliveryAddress
#         fields = ['firstName', 'lastName', 'email']
#         labels = {
#             'firstName': 'Name',
#             'lastName': 'Surname',
#             'email': 'E-mail'
#
#         }
#         widgets = {
#             'firstName': forms.TextInput(attrs={ 'class': 'form-control mb-2'}),
#             'lastName': forms.TextInput(attrs={ 'class': 'form-control mb-2'}),
#             'email': forms.TextInput(attrs={ 'class': 'form-control mb-4', 'type': 'email'})
#         }