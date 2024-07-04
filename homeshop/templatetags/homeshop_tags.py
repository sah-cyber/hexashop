from django import template
from sosialmedia.models import SosialMedia



register = template.Library()

@register.simple_tag()
def get_sosial_mediya():
    return SosialMedia.objects.all()