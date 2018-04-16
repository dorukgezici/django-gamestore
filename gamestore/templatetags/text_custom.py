from django import template

register = template.Library()

def limit_size(text, maxSize):
    if len(text) <= maxSize:
        return text
    else:
        return text[:maxSize-3] + "..."

register.filter('limit_size', limit_size)