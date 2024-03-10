from django.contrib import admin, messages
from .models import Women, Category

# Register your models here.


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'cat', 'is_published', 'brief_info')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'cat')
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    list_filter = ['cat__name', 'is_published']
    search_fields = ['title__startswith', 'cat__name']

    @admin.display(description="Краткое описание", ordering='content')
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        if count == 1:
            self.message_user(request, f"Опубликована {count} запись.")
        self.message_user(request, f"Опубликовано {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        if count == 1:
            self.message_user(request, f"{count} запись снята с публикации!", messages.WARNING)
        self.message_user(request, f"{count} записи(ей) снята с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
