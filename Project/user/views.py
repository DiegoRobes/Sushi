from django.shortcuts import render, redirect
from django.urls import reverse


def register(request):
    context = {}
    return render(request, 'user/register.html')
