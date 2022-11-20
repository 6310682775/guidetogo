from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Tour, Review, BookTour
from users.models import *
from .forms import TourForm
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

# Create your views here.
@login_required(login_url='users:login')
def ChangeStatus(request, pk):
    if request.method == 'POST':
        status = request.POST.get('status')
        bookTour = get_object_or_404(BookTour, id=pk)
        # bookTour = BookTour.objects.get(id=pk) 
        bookTour.verify_member = status
        bookTour.save()
        return HttpResponseRedirect(reverse("tour:profile_tour"))


@method_decorator(login_required, name='dispatch')
class DeleteBookTourMember(DeleteView):
    model = BookTour
    template_name = 'tour/book_delete.html'
    success_url = reverse_lazy('tour:my_tour')

@method_decorator(login_required, name='dispatch')
class TourProfile(ListView):
    model = BookTour
    template_name = "tour/profile_tour.html"
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bookTour = BookTour.objects.filter(tour__guide = self.request.user)
        context['bookTour'] = bookTour
        return context

@login_required(login_url='users:login')
def EnrollTour(request, tour_id):
    if request.method == 'POST':
        this_user = User.objects.get(id=request.user.id)
        this_tour = Tour.objects.get(id=tour_id)
        bookTour = BookTour.objects.create(tour=this_tour,member=this_user)
        bookTour.save()
    return HttpResponseRedirect(reverse('tour:view_tour', args=(this_tour.id,)))

# class create_tour(LoginRequiredMixin, CreateView):
#     model = Tour
#     template_name = "tour/create_tour.html"
#     # fields = '__all__'

#     def form_valid(self, form):
#         form.instance.guide = self.request.user
#         return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class create_tour(LoginRequiredMixin, CreateView):
    model = Tour
    form_class = TourForm
    template_name = "tour/create_tour.html"
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.guide = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class update_tour(UpdateView):
    model = Tour
    form_class = TourForm
    template_name = 'tour/update_tour.html'

@login_required(login_url='users:login')
def my_tour(request):
    if request.user.is_member != True:
        return HttpResponseRedirect(reverse('main:home',))

    check_owner = 0
    my_tour = BookTour.objects.filter(member=request.user).order_by('-created_at')
    return render(request, 'tour/my_tour.html', {
        'my_tour': my_tour,
        'count': my_tour.count(),
        'check_owner': check_owner,
    })

@login_required(login_url='users:login')
def my_tour_guide(request):
    if request.user.is_guide != True:
        return HttpResponseRedirect(reverse('main:home',))

    check_owner = 0
    my_tour = Tour.objects.filter(guide=request.user).order_by('-date')
    return render(request, 'tour/my_tour_guide.html', {
        'my_tour': my_tour,
        'count': my_tour.count(),
        'check_owner': check_owner,
    })

def view_tour(request, tour_id):
    this_tour = get_object_or_404(Tour, id=tour_id)
    this_user = get_object_or_404(User ,id=request.user.id)
    check_owner = 0
    check_booked = True
    if BookTour.objects.filter(tour=this_tour,member=this_user).exists():
        check_booked = False
    if request.user.username == this_tour.guide.username:
        check_owner = 1
    return render(request, 'tour/view_tour.html', context={
        'tour': this_tour,
        'check_owner': check_owner,
        'reviews': Review.objects.filter(review_tour=this_tour),
        'check_booked' : check_booked,
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
def add_review(request, tour_id):
    if request.method == 'POST':
        this_user = User.objects.get(id=request.user.id)
        this_tour = Tour.objects.get(id=tour_id)
        review = Review.objects.create(
            review_user = this_user,
            review_title = request.POST.get('review_title'),
            review_text = request.POST.get('review_text'),
            rating = request.POST.get('rate'),
        )
        review.review_tour.add(this_tour),
        review.save()
        this_tour.review.add(review)
    return HttpResponseRedirect(reverse('tour:view_tour', args=(this_tour.id,)))

@login_required(login_url='users:login')
def remove_review(request, review_id,):
    this_review = Review.objects.get(id=review_id)
    if request.user.username == this_review.review_user.username or request.user.is_superuser == True:
        this_review.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
