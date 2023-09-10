from django import template

register = template.Library()

@register.simple_tag
def mediapath(value):
    if value:
        return f'/media/{value}'
    return '/static/not_found.png'

@register.filter()
def mediapath(val):
	if val:
		return f'/media/{val}'
	return '/static/not_found.png'
