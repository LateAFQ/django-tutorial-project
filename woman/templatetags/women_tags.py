from django import template

from woman.models import TagPost

register = template.Library()


@register.inclusion_tag('woman/list_tags.html')
def show_categories():
    return {"tags": TagPost.objects.all()}