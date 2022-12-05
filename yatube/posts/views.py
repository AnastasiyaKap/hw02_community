from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    title = 'Последние объявления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = f'Записи сообщества {slug}'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': 'Лев Толстой - зеркало русской души ',
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
