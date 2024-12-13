from django.shortcuts import render
from rest_framework import generics,status
from .models import BlogPost,User
from rest_framework.response import Response
from .serializer import BlogPostSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

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





@api_view(['GET'])
def get_user(request):
    user_data={'name':'martin', 'password':'4321', 'email':'test@test.com'}
    serializer=UserSerializer(data=user_data)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(UserSerializer(user_data).data)

    
