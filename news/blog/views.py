from django.http import HttpResponse
from .models import Category, Post
from django.shortcuts import render


def all_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, "blog/index.html", context=context)

