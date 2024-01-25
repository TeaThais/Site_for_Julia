from django.urls import path
from tarotmagic import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('polytheism/', views.polytheism, name='polytheism'),
    path('magic/', views.magic, name='magic'),
    path('tarot/', views.tarot, name='tarot'),
    path('magic/search/', views.magic_search, name='magic_search'),
    path('polytheism/search/', views.polytheism_search, name='polytheism_search'),

    path('tarot/search/', views.tarot_search, name='tarot_search'),
    path('polytheism/<slug:post_slug>/', views.polytheism_show_post, name='polytheism_posts'),
    path('magic/<slug:post_slug>/', views.magic_show_post, name='magic_posts'),
    path('tarot/<slug:post_slug>/', views.tarot_show_post, name='tarot_posts'),
    path('interesting/', views.interesting, name='interesting'),
    path('contact/', views.contact, name='contact'),
]