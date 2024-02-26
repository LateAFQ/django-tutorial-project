from django.urls import reverse

from django.db import models


class PublishedModel (models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


# Create your models here.
class Women (models.Model):
    class Status (models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    objects = models.Manager()
    published = PublishedModel()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})