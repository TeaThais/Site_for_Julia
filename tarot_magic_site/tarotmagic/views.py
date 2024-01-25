from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from tarotmagic.models import Polytheism, Tarot, Magic, Offer, MainPage

# Create your views here.

menu = [
    {'title': 'HOME', 'url_name': 'home'},
    {'title': 'SERVICES', 'url_name': 'services'},
    {'title': 'FEEDBACK', 'url_name': 'interesting'},
    {'title': 'CONTACT', 'url_name': 'contact'},
]

# data_db = [
#     {'id': 1, 'title': 'TAROT', 'content': 'Here you can order my tarot spreads.'},
#     {'id': 2, 'title': 'MAGIC', 'content': 'Here you can order magic rituals.'},
#     {'id': 3, 'title': 'POLYTHEISM', 'content': 'Here you can read about polytheism.'},
# ]


def index(request):
    my_post = get_object_or_404(MainPage)
    data = {
        'title': 'Main page',
        'menu': menu,
        'my_post': my_post
    }
    return render(request, 'tarotmagic/index.html', context=data)


def services(request):
    offers = Offer.objects.all()
    data = {
        'title': 'Services',
        'menu': menu,
        'offers': offers,
    }
    return render(request, 'tarotmagic/services.html', context=data)


def polytheism(request):
    posts = Polytheism.published.all()
    offers = get_object_or_404(Offer, id=3)
    data = {
        'title': 'POLYTHEISM',
        'menu': menu,
        'posts': posts,
        'offers': offers
    }
    return render(request, 'tarotmagic/polytheism.html', context=data)


def polytheism_search(request):
    if request.method == 'POST':
        search_str = request.POST.get('name', None)
        if search_str:
            results = Polytheism.objects.filter(Q(title__contains=search_str.capitalize())
                                                | Q(content__contains=search_str.capitalize())
                                                | Q(title__contains=search_str)
                                                | Q(content__contains=search_str))
            offers = get_object_or_404(Offer, id=3)
            data = {
                'title': 'POLYTHEISM',
                'menu': menu,
                'posts': results,
                'offers': offers
                }
            return render(request, 'tarotmagic/polytheism_search.html', context=data)


def magic(request):
    posts = Magic.published.all()
    offers = get_object_or_404(Offer, id=2)
    data = {
        'title': 'MAGIC',
        'menu': menu,
        'posts': posts,
        'offers': offers
    }
    return render(request, 'tarotmagic/magic.html', context=data)


def magic_search(request):
    if request.method == 'POST':
        search_str = request.POST.get('name', None)
        if search_str:
            results = Magic.objects.filter(Q(title__contains=search_str.capitalize())
                                                | Q(content__contains=search_str.capitalize())
                                                | Q(title__contains=search_str)
                                                | Q(content__contains=search_str))
            offers = get_object_or_404(Offer, id=2)
            data = {
                'title': 'MAGIC',
                'menu': menu,
                'posts': results,
                'offers': offers
                }
            return render(request, 'tarotmagic/magic_search.html', context=data)


def tarot(request):
    posts = Tarot.published.all()
    offers = get_object_or_404(Offer, id=1)
    data = {
        'title': 'TAROT',
        'menu': menu,
        'posts': posts,
        'offers': offers
    }
    return render(request, 'tarotmagic/tarot.html', context=data)


def tarot_search(request):
    if request.method == 'POST':
        search_str = request.POST.get('name', None)
        if search_str:
            results = Tarot.objects.filter(Q(title__contains=search_str.capitalize())
                                                | Q(content__contains=search_str.capitalize())
                                                | Q(title__contains=search_str)
                                                | Q(content__contains=search_str))
            offers = get_object_or_404(Offer, id=1)
            data = {
                'title': 'TAROT',
                'menu': menu,
                'posts': results,
                'offers': offers
                }
            return render(request, 'tarotmagic/tarot_search.html', context=data)


def polytheism_show_post(request, post_slug):
    post = get_object_or_404(Polytheism, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post
    }

    return render(request, 'tarotmagic/post_polytheism.html', context=data)


def magic_show_post(request, post_slug):
    post = get_object_or_404(Magic, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post
    }

    return render(request, 'tarotmagic/post_magic.html', context=data)


def tarot_show_post(request, post_slug):
    post = get_object_or_404(Tarot, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post
    }

    return render(request, 'tarotmagic/post_tarot.html', context=data)


def interesting(request):
    data = {
        'title': 'Interesting',
        'menu': menu
    }
    return render(request, 'tarotmagic/feedback.html', context=data)


def contact(request):
    data = {
        'title': 'Contact',
        'menu': menu
    }
    return render(request, 'base.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('There is no page like this')