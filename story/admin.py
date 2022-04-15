from django.contrib import admin

from .models import Story, Chapter


class ChapterAdminInline(admin.StackedInline):
    model = Chapter
    extra = 0


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [ChapterAdminInline]
