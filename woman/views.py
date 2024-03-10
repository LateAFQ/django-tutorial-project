from django.urls import reverse
from django.shortcuts import render, HttpResponse, Http404, redirect, get_object_or_404
from django.template.defaultfilters import cut

from .models import Women, Category, TagPost

menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}]


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
    cats = Category.objects.all()
    data = {
        'title': post.title,
        'menu': menu,
        'cats': cats,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'woman/post.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    cats = Category.objects.all()
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'posts': posts,
        'menu': menu,
        'cats': cats

    }
    return render(request, 'woman/index.html', context=data)


def contact(request):
    cats = Category.objects.all()
    html_data = {
        'title': 'my_django_server',
        'cats': cats,
        'menu': menu,

    }
    return render(request, 'woman/contact.html', context=html_data)


def addpage(request):
    cats = Category.objects.all()
    html_data = {
        'title': 'my_django_server',
        'cats': cats,
        'menu': menu,
    }
    return render(request, 'woman/add_page.html', context=html_data)


def login(request):
    cats = Category.objects.all()
    html_data = {
        'menu': menu,
        'cats': cats
    }
    return render(request, 'woman/login.html', context=html_data)


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')
