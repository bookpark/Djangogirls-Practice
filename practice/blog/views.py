from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)
