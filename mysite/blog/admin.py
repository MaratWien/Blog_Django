from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # порядок отображения постов
    list_filter = ['status', 'created', 'publish', 'author']  # колонка для фильтрации
    search_fields = ['title', 'body']  # критерии поиска
    prepopulated_fields = {'slug': ('title',)}  # автозаполннения поля {"поле которое заполниться": "зависимость"}
    raw_id_fields = ['author']  # выбор айди автора поста при создании
    date_hierarchy = 'publish'  # навигационные ссылки по иерархии дат
    ordering = ['status', 'publish']  # сортировка, задаются критерии упорядочивания по умолчанию
