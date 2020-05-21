from django.contrib.auth import get_user_model
from blog.models import Posts, Comments
from rest_framework import serializers


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ['user', 'comment', 'date_comment']


class PostsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, required=False)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Posts
        fields = ['id', 'author', 'title', 'subject', 'date_post', 'comments']


class UserSerializer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'posts']

