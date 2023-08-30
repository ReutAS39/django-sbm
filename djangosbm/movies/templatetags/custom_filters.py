from django import template

register = template.Library()


@register.filter()
def digit(value):
    if value:
        return '{0:,}'.format(value).replace(',', ' ')
    else:
        return '-'
