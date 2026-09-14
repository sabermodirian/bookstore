
from django import template

register = template.Library()

# lowercase
@register.filter(name = 'to_low')
def to_lowercase(value1, value2):
	return f'{value2} : {value1.lower()}'
