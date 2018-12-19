from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='get_group')
def get_group(user):
    return user.groups.all()[0].name
