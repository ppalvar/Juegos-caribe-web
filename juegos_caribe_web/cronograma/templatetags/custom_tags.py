from django import template
from django.utils import timezone
register = template.Library()

@register.filter(name="strftime")
def strftime(obj , arg):
    print(obj)
    return timezone.datetime.fromisoformat(obj).strftime(arg)