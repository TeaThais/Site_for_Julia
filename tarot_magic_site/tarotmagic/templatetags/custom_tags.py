from django import template
import tarotmagic.views as views
from tarotmagic.models import Offer

register = template.Library()


@register.inclusion_tag('tarotmagic/includes/navbar_menu.html')
def show_navbar_menu():
    services = Offer.objects.all()
    return {'services': services}