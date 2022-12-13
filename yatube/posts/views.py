from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBERS_LAST_POST = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('group')[:NUMBERS_LAST_POST]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBERS_LAST_POST]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
