from django.urls import path, register_converter
from . import views
from . import converters as cnv

register_converter(cnv.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('cats/', views.categories, name='cats'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_by_slug'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]
