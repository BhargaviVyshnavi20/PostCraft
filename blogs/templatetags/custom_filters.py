from django import template
from django.contrib.humanize.templatetags.humanize import naturaltime

register = template.Library()

@register.filter
def exact_naturaltime(value):
    """
    Takes '2 days, 2 hours ago' and returns '2 days ago'
    """
    if not value:
        return ""
    
    nt = str(naturaltime(value))
    if ',' in nt:
        parts = nt.split(',')
        if nt.endswith(' ago'):
            return parts[0] + ' ago'
        return parts[0]
    return nt
