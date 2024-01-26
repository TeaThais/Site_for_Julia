from django.contrib import admin, messages
from django.utils.safestring import mark_safe

# Register your models here.
from .models import MainPage, Offer, Polytheism, Magic, Tarot, Status

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Моя админка"


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'post_image', 'content')
    list_display = ('id', 'title', 'post_image',  'image', 'content')
    list_display_links = ('title', )
    readonly_fields = ('post_image', )

    def post_image(self, main: MainPage):
        if main.image:
            return mark_safe(f"<img src='{main.image.url}' width=50>")
        else:
            return 'No image'


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_image', 'image', 'description')
    list_display_links = ('title',)
    readonly_fields = ('post_image', )

    def post_image(self, offer: Offer):
        if offer.image:
            return mark_safe(f"<img src='{offer.image.url}' width=50>")
        else:
            return 'No image'


class Services(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_image', 'image', 'content', 'time_create', 'time_update', 'is_published')
    list_display_links = ('title',)
    ordering = ('time_create', )
    list_per_page = 5
    actions = ('set_published', 'set_draft')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_published',)
    readonly_fields = ('post_image',)

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Status.PUBLISHED)
        self.message_user(request, f"записей опубликовано: {count} ")

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Status.DRAFT)
        self.message_user(request, f"записей снято с публикации: {count}", messages.WARNING)


@admin.register(Polytheism)
class PolytheismAdmin(Services):
    def post_image(self, item: Polytheism):
        if item.image:
            return mark_safe(f"<img src='{item.image.url}' width=50>")
        else:
            return 'No image'


@admin.register(Magic)
class MagicAdmin(Services):
    def post_image(self, item: Magic):
        if item.image:
            return mark_safe(f"<img src='{item.image.url}' width=50>")
        else:
            return 'No image'


@admin.register(Tarot)
class TarotAdmin(Services):
    def post_image(self, item: Tarot):
        if item.image:
            return mark_safe(f"<img src='{item.image.url}' width=50>")
        else:
            return 'No image'