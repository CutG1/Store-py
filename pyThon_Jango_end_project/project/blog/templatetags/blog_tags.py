from django import template
from blog.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_sorters():
    sorters = {
        '-views': 'views ⬆',
        'views': 'viewss ⬇',
        '-title': 'from A to Z',
        'title': 'from Z to A',
        '-created_at': 'New movies',
        'created_at': 'Older'
    }
    return sorters