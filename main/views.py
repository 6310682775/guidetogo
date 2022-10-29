from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html' , {
        'main' : []
    })

def about(request):
    return render(request, 'main/about.html')
