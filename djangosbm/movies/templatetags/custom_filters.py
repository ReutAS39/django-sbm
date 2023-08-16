from django import template

register = template.Library()

@register.filter()
def digit(value):
    n = str(value)[::-1]
    b = ' '.join(n[i:i + 3] for i in range(0, len(n), 3))[::-1]
    return b
