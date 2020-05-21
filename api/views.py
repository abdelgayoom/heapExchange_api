from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostsSerializer, CommentsSerializer, UserSerializer
from blog.models import Posts, Comments
from .permissions import IsPostAuthorOrReadOnly, IsCommentAuthorOrReadOnly


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    
class PostsListView(generics.ListCreateAPIView):

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsPostAuthorOrReadOnly
    ]

    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentsListView(generics.ListCreateAPIView):

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsCommentAuthorOrReadOnly
    ]

    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



