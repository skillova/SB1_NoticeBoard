from django.contrib import admin

from announcements.models import Announcement, Comment


@admin.register(Announcement)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description', 'author',)
    list_display_links = ('title',)


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'ad', 'created_at',)
