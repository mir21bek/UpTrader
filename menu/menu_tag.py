from django import template
from django.urls import resolve
from .models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).prefetch_related('children__parent')

    current_path = resolve(request.path_info).url_name
    return {'menu_items': menu_items, 'current_path': current_path}
