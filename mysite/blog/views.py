from django.shortcuts import render
from django.views import generic 
from .serializers import PostSerializer
from rest_framework import viewsets
from .models import Post 
 
class PostList(generic.ListView): 
    queryset = Post.objects.filter(status=1).order_by('-created_on') 
    template_name = 'index.html' 

class PostDetail(generic.DetailView): 
    model = Post 
    template_name = 'post_detail.html' 

class PostViewSet(viewsets.ModelViewSet): 
    serializer_class = PostSerializer 
    queryset = Post.objects.all() 
# Create your views here.
