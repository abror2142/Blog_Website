from django.http import HttpResponse
from .models import Category, Post
from django.shortcuts import render, redirect
from .forms import PostForm, CategoryForm


def all_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, "blog/index.html", context=context)


def all_posts_by_category_id(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, "blog/index.html", context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context=context)


def post_create(request):
    form = PostForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/general_form.html', context=context)


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(data=request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/general_form.html', {'form': form})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/post_delete.html', {"post": post})


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'category': category
    }
    return render(request, 'blog/category_detail.html', context=context)


def category_create(request):
    form = CategoryForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'blog/general_form.html', context=context)


def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(data=request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/general_form.html', {'form': form})


def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'blog/category_delete.html', {"category": category})
