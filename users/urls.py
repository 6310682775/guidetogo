from django.urls import path
from .import  views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'users'
urlpatterns=[
     path('member_register/',views.member_register.as_view(), name='member_register'),
     path('guide_register/',views.guide_register.as_view(), name='guide_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('guide_profile/',views.guide_profile_view, name='guide_profile'),
     path('member_profile/',views.member_profile_view, name='member_profile'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)