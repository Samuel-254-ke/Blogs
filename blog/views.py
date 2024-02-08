from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

""" posts = [
    {
        'author':"Samuel",
        'title':"first Post",
        'content':"First posted content",
        'date_posted':"February 1, 2024"
    },
    {
        'author':"Samira",
        'title':"second Post",
        'content':"second posted content",
        'date_posted':"February 3, 2024"
    }
] """

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
    
