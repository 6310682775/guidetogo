from django.urls import path, include
from .import  views
app_name = 'users'
urlpatterns=[
     path('member_register/',views.member_register.as_view(), name='member_register'),
     path('guide_register/',views.guide_register.as_view(), name='guide_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('guide_profile/',views.guide_profile_view, name='guide_profile'),
     path('guide_profile_edit/',views.guide_profile_edit, name='guide_profile_edit'),
     path('member_profile/',views.member_profile_view, name='member_profile'),
     path('member_profile_edit/', views.member_profile_edit, name='member_profile_edit'),
     path('verified/', views.VerifiedGuide, name='verified_guide'),
     path('profile/<int:pk>', views.ChangeStatus, name='change_status'),
]