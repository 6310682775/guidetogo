from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [
    # path('', views.tour_page, name='tour_page'),
    path('create_tour', views.create_tour, name='create_tour'),
    path('my_tour', views.my_tour, name='my_tour'),
    path('review', views.addreview , name='addreview'),
    path('view_tour/<int:tour_id>', views.view_tour, name='view_tour'),
    path('update_tour/<int:tour_id>', views.update_tour, name='update_tour'),
    path('remove_tour/<int:tour_id>', views.remove_tour, name='remove_tour'),
    
]
