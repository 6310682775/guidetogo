from django.urls import path
from . import views
from .views import ArticleHome, ArticleDetail, AddArticle, UpdateArticle, DeleteArticle, AddCategory, CategoryView, LikeView

app_name = 'article'

urlpatterns = [
    # path('', views.article_home, name='article_home'),
    path('', ArticleHome.as_view(), name='article_home'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('add/', AddArticle.as_view(), name='article_add'),
    path('category/add/', AddCategory.as_view(), name='category_add'),
    path('category/<str:cats>/', CategoryView, name='category_view'),
    path('update/<int:pk>', UpdateArticle.as_view(), name='article_update'),
    path('delete/<int:pk>', DeleteArticle.as_view(), name='article_delete'),
    path('like/<int:pk>', LikeView, name='like_article'),
]