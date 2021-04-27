from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Done',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
