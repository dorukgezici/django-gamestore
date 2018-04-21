from django import template

register = template.Library()


def limit_size(text, max_size):
    if len(text) <= max_size:
        return text
    else:
        return text[:max_size-3] + "..."


register.filter('limit_size', limit_size)


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
