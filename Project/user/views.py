from django.shortcuts import render, redirect
from django.urls import reverse


def sign_up(request):
    context = {}
    return render(request, 'user/sign_up.html')
