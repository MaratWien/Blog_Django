from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from .models import Post


def post_list(request) -> HttpResponse:
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id: int) -> HttpResponse:
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)

    return render(request, 'blog/post/detail.html', {'posts': post})
