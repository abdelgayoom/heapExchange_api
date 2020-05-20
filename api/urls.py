from django.urls import path
from . import views

urlpatterns = [

    path('post/', views.PostsListView.as_view()),
    path('post/<int:pk>/', views.PostsDetailView.as_view()),
    path('post/<int:pk>/comments/', views.CommentsListView.as_view()),

]