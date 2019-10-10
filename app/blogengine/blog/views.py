from django.shortcuts import render
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectsDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectsDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectsDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
