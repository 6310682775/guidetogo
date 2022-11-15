from django.urls import path
from . import views
# from .views import CreateTour

app_name = 'tour'

urlpatterns = [

    path('add_review/<int:tour_id>', views.add_review , name='add_review'),
    path('remove_review/<int:review_id>', views.remove_review , name='remove_review'),
    path('create_tour', views.create_tour.as_view(), name='create_tour'),
    path('my_tour/member', views.my_tour, name='my_tour'),
    path('my_tour/guide', views.my_tour_guide, name='my_tour_guide'),
    path('view_tour/<int:tour_id>', views.view_tour, name='view_tour'),
    path('update_tour/<int:pk>/', views.update_tour.as_view(), name='update_tour'),
    path('remove_tour/<int:tour_id>', views.remove_tour, name='remove_tour'),
    path('profile', views.TourProfile.as_view(), name='profile_tour'),
    path('profile/<int:pk>', views.ChangeStatus, name='change_status'),
    path('view_tour/book/<int:tour_id>', views.EnrollTour, name='book_tour'),
]
