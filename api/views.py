from rest_framework import generics
from rest_framework import permissions
from .serializers import PostsSerializer, CommentsSerializer
from blog.models import Posts, Comments
from .permissions import IsOwnerOrReadOnly


class PostsListView(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsListView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()






