from django.shortcuts import render
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.urls import reverse
from tour.models import Tour, Review
from users.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from .filters import Tourfilter
# Create your views here.

def home(request):
    all_tour = Tour.objects.all()
    myFilter = Tourfilter(request.GET, queryset = all_tour)
    all_tour = myFilter.qs
    
    popular_tour = Tour.objects.annotate(num_review= Count('review')).order_by('-num_review')[:8]

    return render(request, 'main/home.html' , {
        'all_tour' : all_tour,
        'myFilter': myFilter,
        'popular_tour':popular_tour,  
    })

def about(request):
    return render(request, 'main/about.html')
