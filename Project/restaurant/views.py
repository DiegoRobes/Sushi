from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def home(request):
    context = {}
    return render(request, "restaurant/index.html", context=context)





