from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializer import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostList(APIView):
    def get(self, request, format=None):

        title=request.query_params.get("title","")

        if title:
            blog_post = BlogPost.objects.filter(title_icontains=title)

        else:
            blog_post = BlogPost.objects.all()
        serializer=BlogPostSerializer(blog_post,many=True)
        return Response(serializer.data)
