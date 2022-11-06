from django.shortcuts import render

from django.shortcuts import render, redirect
from django.urls import reverse
from tour.models import Tour, Review
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    all_tour = Tour.objects.all()
    return render(request, 'main/home.html' , {
        'all_tour' : all_tour,
    })

def about(request):
    return render(request, 'main/about.html')
