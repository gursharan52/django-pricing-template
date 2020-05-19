from django.shortcuts import render
from .models import subsciption, subscriber
from http import *


def price(request):
    obj= subsciption.objects.all()  
    return render(request, 'home.html', {'data':obj})


def subscriber_price(request):
    obj= subscriber.objects.all()  
    return render(request, 'subscriber.html', {'data':obj})
    




