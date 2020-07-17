# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignupView(CreateView):
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
