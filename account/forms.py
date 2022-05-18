# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.contrib.auth.models import User
# from django import forms
#
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(CreateUserForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#              visible.field.widget.attrs['class'] = 'form-control'
#
# class EditUserForm(UserChangeForm):
#     password = None
#
#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name']
#
#     def __init__(self, *args, **kwargs):
#         super(EditUserForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#              visible.field.widget.attrs['class'] = 'form-control'
#
# class ChangePasswordForm(PasswordChangeForm):
#     def __init__(self, *args, **kwargs):
#         super(ChangePasswordForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#              visible.field.widget.attrs['class'] = 'form-control'