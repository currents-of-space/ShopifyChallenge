# from django.forms import ModelForm, TextInput
# from django import forms
# from .models import FilterProduct
#
#
# class FilterForm(ModelForm):
#     class Meta:
#         model = FilterProduct
#         fields = ['filterChoice', 'isOnSale', 'isAvailable']
#         labels = {
#             'isOnSale': 'Discount',
#             'isAvailable': 'Only Available'
#         }
#         widgets = {
#             'filterChoice': forms.Select(attrs={ 'class': 'form-select'}),
#             'isOnSale': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'isOnSale'}),
#             'isAvailable': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'isAvailable'})
#         }