from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date =models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='alex@gmail.com')
    password = models.CharField(max_length=100)
    age = models.IntegerField

    def __str__(self):
        return self.name

    


