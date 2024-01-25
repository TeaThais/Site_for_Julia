from django.contrib import admin, messages

# Register your models here.
from .models import MainPage, Offer, Polytheism, Magic, Tarot, Status

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Моя админка"


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','image', 'content')
    list_display_links = ('title', )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','image', 'description')
    list_display_links = ('title',)


class Services(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'content', 'time_create', 'time_update', 'is_published')
    list_display_links = ('title',)
    ordering = ('time_create', )
    list_per_page = 5
    actions = ('set_published', 'set_draft')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ('is_published',)


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
    pass


@admin.register(Magic)
class MagicAdmin(Services):
    pass


@admin.register(Tarot)
class TarotAdmin(Services):
    pass
