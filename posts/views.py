from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

# Create your views here.


def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)


def posts_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id:
            posts = Post.objects.filter(category_id=category_id)
        else:
            posts = Post.objects.all()

        data = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=data)
