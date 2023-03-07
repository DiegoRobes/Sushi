from django.shortcuts import render, redirect
from django.urls import reverse


def welcome(request):
    context = {}
    return render(request, 'user/welcome.html')


def login(request):
    context = {}
    return render(request, 'user/login.html')


def sign_up(request):
    context = {}
    return render(request, 'user/sign_up.html')


def my_account(request):
    context = {}
    return render(request, 'user/my_account.html')


