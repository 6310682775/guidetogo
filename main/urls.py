from django.urls import path,include
from . import views
from django.contrib import admin

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('admin/', admin.site.urls),
    
]
