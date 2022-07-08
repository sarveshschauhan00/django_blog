from django.urls import path, include
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCatagoryView, CatagoryView, LikeView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_catagory/', AddCatagoryView.as_view(), name='add_catagory'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('catagory/<str:cat>/', CatagoryView, name='catagory'),
    path('like/<int:pk>', LikeView, name='like_post'),
]