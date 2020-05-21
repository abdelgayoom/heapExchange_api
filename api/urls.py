from django.urls import path
from . import views


urlpatterns = [

    path('post/', views.PostsListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', views.PostsDetailView.as_view(), name='posts-detail'),
    path('users/', views.UserListView.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='users-detail'),
]
