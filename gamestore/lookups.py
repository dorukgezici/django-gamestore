from ajax_select import register, LookupChannel
from .models import Tag

@register('tags')
class TagsLookup(LookupChannel):

    model = Tag

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')[:50]

    def get_result(self, obj):
    	return obj.name

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.name

    def can_add(self, user, model):
    	return True