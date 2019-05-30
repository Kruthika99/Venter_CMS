import ast
from django import template


register = template.Library()

@register.filter
def get_domain_data(dictionary, key):
    p = ast.literal_eval(dictionary)
    return p[key]

@register.filter
def get_domain(value, domain):
    return value.replace(value, domain)
