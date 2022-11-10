from rest_framework.response import Response
from rest_framework.views import APIView

from apps.dashboard.models import Post
from django.shortcuts import render

from .serializer import PostSerializer


class PostListView(APIView):
    """
    Return list of all Posts
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


