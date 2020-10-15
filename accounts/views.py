from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # when successful signup, reverse them back to logon page
    # reverse_lazy doesn't get executed until sibmit is hit
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'