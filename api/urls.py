from django.urls import path
from . import views 
urlpatterns = [
    path('', views.BlogPostListCreate.as_view(), name='blogPostlistCreate'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'), 
    path('user/',views.get_user, name='user'),
      

]