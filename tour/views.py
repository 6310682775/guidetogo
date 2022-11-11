from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Tour, Review
from users.models import *
from .forms import TourForm
from datetime import datetime
# from django.views.generic import CreateView

# Create your views here.

@login_required(login_url='users:login')
def create_tour(request):
    if request.user.is_guide != True:
        return HttpResponseRedirect(reverse('main:home',))

    if request.method == 'POST':

        form = TourForm(request.POST)

        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            tour = Tour.objects.create(guide=user)
            tour.t_name = request.POST['t_title']
            tour.province = request.POST['province']
            tour.price = request.POST['price']
            tour.amount = request.POST['amount']
            tour.period = request.POST['period']
            tour.img = request.POST['img']
            tour.information = request.POST['information']
            tour.save()
            return HttpResponseRedirect(reverse('tour:my_tour'))
    else:
        form = TourForm()

    return render(request, 'tour/create_tour.html', {
        'form': form,
    })

@login_required(login_url='users:login')
def my_tour(request):
    if request.user.is_guide != True and request.user.is_member != True:
        return HttpResponseRedirect(reverse('main:home',))

    check_owner = 0
    my_tour = Tour.objects.filter(guide=request.user).order_by('-date')
    return render(request, 'tour/my_tour.html', {
        'my_tour': my_tour,
        'count': my_tour.count(),
        'check_owner': check_owner,
    })

def view_tour(request, tour_id):
    this_tour = get_object_or_404(Tour, id=tour_id)
    tour_name = tour_id
    check_owner = 0
    if request.user.username == this_tour.guide.username:
        check_owner = 1
    return render(request, 'tour/view_tour.html', {
        'tour': this_tour,
        'check_owner': check_owner,
        "reviews": Review.objects.filter(reviewed_tour=tour_name)
    })
    

@login_required(login_url='users:login')
def update_tour(request, tour_id):
    this_tour = get_object_or_404(Tour, id=tour_id)

    check_update = 1

    initial_data = {
        't_title': this_tour.t_name,
        'province': this_tour.province,
        'price': this_tour.price,
        'amount': this_tour.amount,
        'period': this_tour.period,
        'img': this_tour.img,
        'information': this_tour.information,
    }

    # Check user is own this Tour
    if request.user.username != this_tour.guide.username:
        return HttpResponseRedirect(reverse('tour:my_tour',))
        # return HttpResponseRedirect(reverse('tour:my_tour', args=(this_tour.id,)))

    if request.method == 'POST':
        form = TourForm(initial=initial_data, )
        if form.is_valid():
            
            return HttpResponseRedirect(reverse('tour:view_tour', args=(this_tour.id,)))
        else:
            this_tour.t_name = request.POST['t_title']
            this_tour.province = request.POST['province']
            this_tour.price = request.POST['price']
            this_tour.amount = request.POST['amount']
            this_tour.period = request.POST['period']
            this_tour.img = request.POST['img']
            this_tour.information = request.POST['information']
            this_tour.date = datetime.now()
            this_tour.save()
            return HttpResponseRedirect(reverse('tour:view_tour', args=(this_tour.id,)))

    else:
        form = TourForm(initial=initial_data, )

    return render(request, 'tour/update_tour.html', {
        'form': form,
    })

@login_required(login_url='users:login')
def remove_tour(request, tour_id):
    this_tour = Tour.objects.get(id=tour_id)
    if request.user.username == this_tour.guide.username or request.user.is_superuser == True:
        this_tour.delete()
        return HttpResponseRedirect(reverse('tour:my_tour'))
        # return HttpResponseRedirect(reverse("tour:my_tour", args=(this_tour.tour_id,)))

    return HttpResponseRedirect(reverse('tour:view_tour', args=(this_tour.id,)))

@login_required(login_url='users:login')
def addreview(request):

    if request.method == "POST":
        touruser = User.objects.get(id=request.user.id)
        #touruser = request.POST.get("user")
        usertour = User.objects.get(username=touruser)
        review = Review.objects.create(
            review_name = request.POST.get("name"),
            review_text = request.POST.get("review"),
            rating = request.POST.get("rate"),
        )

        review.reviewed_tour.add(usertour)
        review.save()
    return render(request, "tour/Thankyou.html")

    
