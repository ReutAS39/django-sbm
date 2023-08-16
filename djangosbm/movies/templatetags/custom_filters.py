from django import template

register = template.Library()

@register.filter()
def digit(value):
    return '{0:,}'.format(value).replace(',', ' ')


