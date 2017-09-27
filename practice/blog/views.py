from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)