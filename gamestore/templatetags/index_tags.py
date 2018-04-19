from django import template

register = template.Library()

def limit_size(text, maxSize):
    if len(text) <= maxSize:
        return text
    else:
        return text[:maxSize-3] + "..."

register.filter('limit_size', limit_size)


@register.simple_tag
def url_replace(request, field, value):

    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()