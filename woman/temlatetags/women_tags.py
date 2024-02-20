from django import template
import woman.views as views

register = template.Library()


@register.inclusion_tag('women/list_categories')
def show_categories():
    pass