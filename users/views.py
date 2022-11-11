from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Member, Guide
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

class member_register(CreateView):
    model = User
    form_class = MemberSignUpForm
    template_name = 'users/member_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class guide_register(CreateView):
    model = User
    form_class = GuideSignUpForm
    template_name = 'users/guide_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:home'))

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'users/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('main:home')

@login_required(login_url='users:login')
def member_profile_view(request):
    if request.user.is_member != True:
        return HttpResponseRedirect(reverse('main:home',))
    return render(request, "users/member_profile.html")

@login_required(login_url='users:login')
def guide_profile_view(request):
    if request.user.is_guide != True:
        return HttpResponseRedirect(reverse('main:home',))
    return render(request, "users/guide_profile.html")

############################
@login_required(login_url='users:login')
def member_profile_edit(request):
    if request.method == 'POST':
        user_form = UpdateMemberForm(request.POST, instance=request.user)
        mem_form = UpdateMemberForm(request.POST, instance=request.user.member)

        if user_form.is_valid():
            user_form.save()
            mem_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:member_profile')
    else:
        user_form = UpdateMemberForm(instance=request.user)
        mem_form = UpdateMemberForm(instance=request.user.member)

    return render(request, 'users/member_profile_edit.html', {
        'user_form': user_form,
        'mem_form' : mem_form,
    })


@login_required(login_url='users:login')
def guide_profile_edit(request):
    if request.method == 'POST':
        user_form = UpdateGuideForm(request.POST, request.FILES, instance=request.user)
        guide_form = UpdateGuideForm(request.POST, request.FILES, instance=request.user.guide)

        if user_form.is_valid():
            user_form.save()
            guide_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:guide_profile')
    else:
        user_form = UpdateGuideForm(instance=request.user)
        guide_form = UpdateGuideForm(instance=request.user.guide)

    return render(request, 'users/guide_profile_edit.html', {
        'user_form': user_form,
        'guide_form' : guide_form,
    })
    


    