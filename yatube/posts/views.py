from django.shortcuts import get_object_or_404, render

from django.core.paginator import Paginator

from .models import Group, Post, User

NUMBERS_POSTS_ON_PAGES = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter()[:NUMBERS_POSTS_ON_PAGES]
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'group': group
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    posts_count = posts.count()
    paginator = Paginator(posts, NUMBERS_POSTS_ON_PAGES)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = f'Профайл пользователя {user.username}'
    context = {
        'user': user,
        'post_list': posts,
        'page_obj': page_obj,
        'posts_count': posts_count,
        'title': title
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts_list = (Post.objects.select_related('author')
                  .filter(author=post.author))
    posts_count = posts_list.count()
    context = {
        'post': post,
        'posts_count': posts_count
    }
    return render(request, 'posts/post_detail.html', context)
