from django.urls import reverse
from django.shortcuts import render, HttpResponse, Http404, redirect
from django.template.defaultfilters import cut

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
    html_data = {
        'title': 'my_django_server',
        'menu': menu,
        'posts': data_db
    }

    return render(request, 'woman/index.html', context=html_data)


def about(request):
    html_data = {'title': 'О сайте'}
    return render(request, 'woman/about.html', html_data)


def categories(request):
    return HttpResponse('<h1>Статьи по категориям')


def archive(request, year):
    if year > 2024:
        uri = reverse('cats_by_slug', args=['HelloSlug'])
        return redirect(uri)
    return HttpResponse(f'<h1> Статьи по категориям</h1><p>{year}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1> Статьи по категориям</h1><p>slug:{cat_slug}</p>')


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
        'menu': menu,
        'TEST': 1
    }
    return render(request, 'woman/login.html', context=html_data)


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена')

