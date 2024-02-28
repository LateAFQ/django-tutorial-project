from django.urls import reverse
from django.shortcuts import render, HttpResponse, Http404, redirect, get_object_or_404
from django.template.defaultfilters import cut

from .models import Women, Category

menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
    ]


def index(request):
    cats = Category.objects.all()
    posts = Women.objects.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'cats': cats,
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'woman/index.html', context=data)


def about(request):
    html_data = {'title': 'О сайте'}
    return render(request, 'woman/about.html', html_data)


def show_category(request, cat_slug):
    cats = Category.objects.all()
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(is_published=1, cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'cats': cats,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'woman/index.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'woman/post.html', context=data)


def contact(request):
    html_data = {
        'title': 'my_django_server',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'woman/contact.html', context=html_data)


def addpage(request):
    html_data = {
        'title': 'my_django_server',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'woman/add_page.html', context=html_data)


def login(request):
    html_data = {
        'menu': menu
    }
    return render(request, 'woman/login.html', context=html_data)


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')

