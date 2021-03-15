from django.contrib import admin
from .models import Song, Tag


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'artist', 'year')
    search_fields = ('title', 'author')
    list_filter = ('year',)


@admin.register(Tag)
class SongAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'style')
    search_fields = ('title', 'author')
    list_filter = ('title',)
