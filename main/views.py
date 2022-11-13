from django.shortcuts import render

from django.shortcuts import render, redirect
from django.urls import reverse
from tour.models import Tour, Review
from django.http import HttpResponseRedirect
from .filters import Tourfilter
# Create your views here.

def home(request):
    all_tour = Tour.objects.all()

    myFilter = Tourfilter(request.GET, queryset = all_tour)
    all_tour = myFilter.qs

    return render(request, 'main/home.html' , {
        'all_tour' : all_tour,
        'myFilter': myFilter,
    })

def about(request):
    return render(request, 'main/about.html')
